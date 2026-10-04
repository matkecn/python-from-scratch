"""Small integers.

Integers are whole numbers with no decimal part.

Run me:
    python 858-small-integers/lesson_858_small_integers.py
"""

from __future__ import annotations


def whole_pairs(count: int) -> int:
    """Return how many whole pairs a count makes.

    Args:
        count: How many things there are.

    Returns:
        The number of whole pairs.

    Examples:
        >>> whole_pairs(7)
        3
    """
    return count // 2


def is_even(number: int) -> bool:
    """Say whether a number divides by two with nothing left over.

    Args:
        number: The number to check.

    Returns:
        ``True`` when the number is even.

    Examples:
        >>> is_even(4)
        True
    """
    return number % 2 == 0


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(whole_pairs(7))
    print(is_even(4))


if __name__ == "__main__":
    main()
