"""Getting started.

Three commands and you are ready to write Python.

Run me:
    python 001-getting-started/lesson_001_getting_started.py
"""

from __future__ import annotations

import sys

NEEDED = (3, 11)


def version_number() -> tuple[int, int]:
    """Return the Python version as two plain numbers.

    Returns:
        The major and minor version, for example ``(3, 12)``.

    Examples:
        >>> version = version_number()
        >>> len(version)
        2
    """
    return sys.version_info.major, sys.version_info.minor


def is_supported() -> bool:
    """Say whether this Python is new enough for the course.

    Returns:
        ``True`` when the version is 3.11 or newer.

    Examples:
        >>> is_supported() == (version_number() >= (3, 11))
        True
    """
    return version_number() >= NEEDED


def version_text() -> str:
    """Return a friendly one line description of this Python.

    Returns:
        Text such as ``"Python 3.12.0 is ready"``.

    Examples:
        >>> version_text().startswith("Python 3")
        True
    """
    full = ".".join(str(part) for part in sys.version_info[:3])
    if is_supported():
        return f"Python {full} is ready"
    return f"Python {full} is too old, we need {NEEDED[0]}.{NEEDED[1]} or newer"


def main() -> None:
    """Print what we found."""
    print(version_text())


if __name__ == "__main__":
    main()
