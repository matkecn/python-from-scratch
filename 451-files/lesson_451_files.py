"""Files.

Files let your code remember things after it stops.

Run me:
    python 451-files/lesson_451_files.py
"""

from __future__ import annotations


from pathlib import Path


def save_lines(lines: list[str], path: str) -> int:
    """Write lines to a file and return how many were written.

    Args:
        lines: The lines to save.
        path: Where to save them.

    Returns:
        The number of lines written.
    """
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines))
    return len(lines)


def read_lines(path: str) -> list[str]:
    """Read lines back from a file.

    Args:
        path: The file to read.

    Returns:
        The lines that were in the file.
    """
    return Path(path).read_text(encoding="utf-8").splitlines()


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    import tempfile

    folder = tempfile.mkdtemp()
    target = f"{folder}/demo.txt"
    print(save_lines(["one", "two"], target))
    print(read_lines(target))


if __name__ == "__main__":
    main()
