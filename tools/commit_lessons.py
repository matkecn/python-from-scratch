"""Create one commit per lesson folder, one at a time.

Usage::

    python3 tools/commit_lessons.py --dry-run
    python3 tools/commit_lessons.py
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import curriculum  # noqa: E402

TITLE = re.compile(r"^# (\d{3}) · (.+)$", re.MULTILINE)
STATUS = re.compile(r"\*\*Status\*\* (.+?)(?:,| ·|$)", re.MULTILINE)
BLURB = re.compile(r"^# \d{3} · .+\n\n(.+)$", re.MULTILINE)

SPECIAL = {
    "000-meta": (
        "docs",
        "add the course roadmap, contributing guide, licence and integrity test",
        "Section: course meta\nStatus: hand written\n\nThe map of the course and the rules for writing in it: the section\nroadmap, the contribution guide, the licence and a test that checks all 999\nfolders, file names, docstrings and notebook links.",
    ),
    "000-welcome": (
        "feat",
        "add the welcome lesson: your first Python program",
        "Section: course welcome\nStatus: hand written\n\nOne line of Python, explained slowly, with a notebook to click through.",
    ),
}


def prettify(title: str) -> str:
    """Turn a raw slug title into readable words.

    Args:
        title: A title that may still contain slug hyphens.

    Returns:
        The title with each word capitalised.
    """
    if "-" not in title:
        return title
    return " ".join(word if word.isupper() else word.capitalize() for word in title.split("-"))


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    """Run a git command inside the repository.

    Args:
        args: The git arguments.
        check: Whether a non-zero exit code should raise.

    Returns:
        The finished process.
    """
    process = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=False)
    if check and process.returncode != 0:
        raise SystemExit(f"git {' '.join(args)} failed ({process.returncode}):\n{process.stderr.strip()}")
    return process


def describe(folder: Path, topic: curriculum.Topic) -> tuple[str, str, str]:
    """Return the commit scope, body lines and title for one lesson.

    Args:
        folder: The lesson folder.
        topic: The lesson's place in the course.

    Returns:
        The commit scope, the title and the body.
    """
    readme = folder / "README.md"
    title = topic.title
    status = "unknown"
    blurb = ""
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        if match := TITLE.search(text):
            title = prettify(match.group(2).strip())
        if match := STATUS.search(text):
            status = match.group(1).strip()
        elif "generated draft" in text:
            status = "generated draft"
        if match := BLURB.search(text):
            blurb = match.group(1).strip()
    scope = topic.folder
    body = [f"Section: {section_title(topic)}", f"Status: {status}"]
    if blurb:
        body += ["", blurb]
    body += ["", f"Adds {folder.name}/ with README.md, lesson.ipynb and the example module plus its tests."]
    return scope, title, "\n".join(body)


def section_title(topic: curriculum.Topic) -> str:
    """Return the human title of the section a lesson belongs to.

    Args:
        topic: The lesson to look up.

    Returns:
        The section title.
    """
    for section in curriculum.SECTIONS:
        if section.key == topic.section:
            return section.title
    return topic.section


def main() -> int:
    """Commit every lesson folder, one folder per commit.

    Returns:
        The process exit code.
    """
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dry-run", action="store_true", help="print the commits without making them")
    args = parser.parse_args()

    folders = sorted(
        (path for path in ROOT.iterdir() if path.is_dir() and re.fullmatch(r"\d{3}-.+", path.name)),
        key=lambda path: path.name,
    )
    print(f"folders to commit: {len(folders)}")

    for index, folder in enumerate(folders, start=1):
        number = int(folder.name[:3])
        if folder.name in SPECIAL:
            kind, title, body = SPECIAL[folder.name]
            scope = folder.name
            subject = f"{kind}({scope}): {title}"
        else:
            topic = curriculum.TOPICS[number - 1]
            scope, title, body = describe(folder, topic)
            kind = "feat"
            subject = f"{kind}({scope}): add {folder.name[:3]} {title}"
        if args.dry_run:
            print(f"\n{subject}\n\n{body}")
            continue
        git("add", "--", folder.name)
        if git("diff", "--cached", "--quiet", check=False).returncode != 0:
            git("commit", "-q", "--no-gpg-sign", "-m", subject, "-m", body)
        if index % 100 == 0 or index == len(folders):
            print(f"  {index}/{len(folders)} committed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
