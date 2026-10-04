"""What is Python.

Python is two things: a language you write, and a program that runs it.

Run me:
    python 002-what-is-python/lesson_002_what_is_python.py
"""

from __future__ import annotations

import platform
import sys


def implementation() -> str:
    """Return the name of the Python running this code.

    Returns:
        Usually ``"CPython"``.

    Examples:
        >>> isinstance(implementation(), str)
        True
    """
    return platform.python_implementation()


def python_version() -> str:
    """Return the full version, such as ``"3.12.0"``.

    Returns:
        The version as text.
    """
    return platform.python_version()


def runs_bytecode() -> bool:
    """Say whether Python turns source into bytecode before running it.

    Returns:
        ``True`` for CPython, which caches compiled code.

    Examples:
        >>> runs_bytecode() == (implementation() == "CPython")
        True
    """
    return implementation() == "CPython"


def summary() -> str:
    """Return one sentence describing this Python.

    Returns:
        A short summary you could read out loud.
    """
    return f"{implementation()} {python_version()} runs bytecode: {runs_bytecode()}"


def main() -> None:
    """Print what we found."""
    print(summary())
    print(f"running on {sys.platform}")


if __name__ == "__main__":
    main()
