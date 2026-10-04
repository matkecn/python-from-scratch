"""Rewrite one commit message without touching the trees around it.

Usage::

    python3 tools/fix_commit_message.py <commit> <message-file>
"""

from __future__ import annotations

import subprocess
import sys

ROOT = __file__.rsplit("/", 2)[0]


def git(*args: str, stdin: str | None = None) -> str:
    """Run a git command and return its trimmed stdout.

    Args:
        args: The git arguments.
        stdin: Optional text to send to the process.

    Returns:
        The trimmed standard output.
    """
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        input=stdin,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def main() -> int:
    """Replace the message of one commit, keeping every tree identical.

    Returns:
        The process exit code.
    """
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    target, message_file = sys.argv[1], sys.argv[2]
    message = open(message_file, encoding="utf-8").read()
    if not message.endswith("\n"):
        message += "\n"

    commits = git("rev-list", "--reverse", "HEAD").split()
    if target not in commits:
        print(f"{target} is not in HEAD")
        return 1
    before = commits.index(target)
    rewritten: dict[str, str] = {}
    for commit in commits[before:]:
        tree = git("log", "-1", "--format=%T", commit)
        parents = [rewritten.get(p, p) for p in git("log", "-1", "--format=%P", commit).split()]
        author_name = git("log", "-1", "--format=%an", commit)
        author_email = git("log", "-1", "--format=%ae", commit)
        author_date = git("log", "-1", "--format=%aI", commit)
        text = message if commit == target else f"{git('log', '-1', '--format=%B', commit)}\n"
        args = ["commit-tree", tree]
        for parent in parents:
            args += ["-p", parent]
        new = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            input=text,
            capture_output=True,
            text=True,
            check=True,
            env={
                "PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin",
                "HOME": "/tmp",
                "GIT_AUTHOR_NAME": author_name,
                "GIT_AUTHOR_EMAIL": author_email,
                "GIT_AUTHOR_DATE": author_date,
                "GIT_COMMITTER_NAME": author_name,
                "GIT_COMMITTER_EMAIL": author_email,
            },
        ).stdout.strip()
        rewritten[commit] = new

    old_head = git("rev-parse", "HEAD")
    git("update-ref", "refs/heads/main", rewritten[old_head], old_head)
    git("reset", "--hard", "HEAD")
    print(f"rewrote {before + 1} commits; new HEAD {rewritten[old_head][:7]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
