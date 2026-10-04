"""Python versions.

Versions are written like ``3.12.1``: big number, small number, patch number.

Run me:
    python 004-python-versions/lesson_004_python_versions.py
"""

from __future__ import annotations

OLDEST = (3, 11)


def parse_version(text: str) -> tuple[int, int, int]:
    """Turn version text into three numbers.

    Args:
        text: A version such as ``"3.12.1"`` or ``"3.12"``.

    Returns:
        The major, minor and patch numbers, filling in zeros when missing.

    Raises:
        ValueError: If the text does not start with a number.

    Examples:
        >>> parse_version("3.12.1")
        (3, 12, 1)
        >>> parse_version("3.12")
        (3, 12, 0)
    """
    parts = text.strip().split(".")
    try:
        numbers = [int(part) for part in parts[:3]]
    except ValueError as error:
        raise ValueError(f"not a version: {text!r}") from error
    while len(numbers) < 3:
        numbers.append(0)
    return numbers[0], numbers[1], numbers[2]


def compare(first: str, second: str) -> int:
    """Compare two version strings.

    Args:
        first: The version on the left.
        second: The version on the right.

    Returns:
        ``-1`` when first is older, ``0`` when they match, ``1`` when first is newer.

    Examples:
        >>> compare("3.11.0", "3.12.0")
        -1
        >>> compare("3.12.0", "3.12.0")
        0
    """
    left = parse_version(first)
    right = parse_version(second)
    if left < right:
        return -1
    if left > right:
        return 1
    return 0


def needs_upgrade(text: str) -> bool:
    """Say whether a version is too old for this course.

    Args:
        text: The version to check.

    Returns:
        ``True`` when the course needs a newer Python.

    Examples:
        >>> needs_upgrade("3.8.10")
        True
        >>> needs_upgrade("3.13.0")
        False
    """
    major, minor, _patch = parse_version(text)
    return (major, minor) < OLDEST


def main() -> None:
    """Compare two versions out loud."""
    print(f"3.10.0 versus 3.12.0 gives {compare('3.10.0', '3.12.0')}")
    print(f"do we need an upgrade? {needs_upgrade('3.9.1')}")


if __name__ == "__main__":
    main()
