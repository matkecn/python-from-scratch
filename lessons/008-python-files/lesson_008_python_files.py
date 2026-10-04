"""Python files.

A Python program is a text file with a ``.py`` ending. That is all it is.

Run me:
    python 008-python-files/lesson_008_python_files.py
"""

from __future__ import annotations

from pathlib import Path


def write_script(path: str, lines: list[str]) -> int:
    """Write some lines into a Python file.

    Args:
        path: Where to write the file.
        lines: The lines to write.

    Returns:
        The number of lines written.
    """
    text = "\n".join(lines) + "\n"
    Path(path).write_text(text, encoding="utf-8")
    return len(lines)


def read_script(path: str) -> list[str]:
    """Read a Python file back line by line.

    Args:
        path: The file to read.

    Returns:
        The lines, without their line endings.
    """
    return Path(path).read_text(encoding="utf-8").splitlines()


def count_lines(path: str) -> int:
    """Count the lines in a file.

    Args:
        path: The file to count.

    Returns:
        How many lines it holds.
    """
    return len(read_script(path))


def is_python_file(path: str) -> bool:
    """Say whether a name looks like a Python file.

    Args:
        path: The file name to check.

    Returns:
        ``True`` when the name ends with ``.py``.

    Examples:
        >>> is_python_file("game.py")
        True
        >>> is_python_file("game.txt")
        False
    """
    return path.endswith(".py")


def main() -> None:
    """Make a file, read it back, then delete it."""
    import tempfile
    from pathlib import Path as RealPath

    target = str(RealPath(tempfile.mkdtemp()) / "demo.py")
    write_script(target, ["print('hi')", "print('bye')"])
    print(read_script(target))
    print(f"{count_lines(target)} lines, python file: {is_python_file(target)}")
    RealPath(target).unlink()


if __name__ == "__main__":
    main()
