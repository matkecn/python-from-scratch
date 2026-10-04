"""Installation.

Is Python installed? This lesson asks the computer instead of guessing.

Run me:
    python 003-installation/lesson_003_installation.py
"""

from __future__ import annotations

import shutil
import sys


def find_python() -> str:
    """Return the path of a Python program on this computer.

    Returns:
        The path of ``python3``, or the interpreter running this code.

    Examples:
        >>> bool(find_python())
        True
    """
    return shutil.which("python3") or sys.executable


def is_installed() -> bool:
    """Say whether a Python program can be found.

    Returns:
        ``True`` when Python is ready to use.
    """
    return bool(find_python())


def check() -> str:
    """Return a short report about this computer.

    Returns:
        A line a beginner can read without panic.
    """
    if not is_installed():
        return "Python is missing. Install it from python.org and try again."
    return f"Python found at {find_python()}"


def main() -> None:
    """Print the report."""
    print(check())


if __name__ == "__main__":
    main()
