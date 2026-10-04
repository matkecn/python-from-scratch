"""Booleans.

Booleans are just two values: `True` and `False`.

Run me:
    python 024-booleans/lesson_024_booleans.py
"""

from __future__ import annotations


def is_odd(number: int) -> bool:
    """Say whether a number is odd.

    Args:
        number: The number to check.

    Returns:
        ``True`` when the number is odd.

    Examples:
        >>> is_odd(3)
        True
    """
    return number % 2 == 1


def both_yes(first: bool, second: bool) -> bool:
    """Say whether both answers are yes.

    Args:
        first: The first yes or no.
        second: The second yes or no.

    Returns:
        ``True`` only when both are ``True``.

    Examples:
        >>> both_yes(True, False)
        False
    """
    return first and second


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(is_odd(3))
    print(both_yes(True, False))


if __name__ == "__main__":
    main()
