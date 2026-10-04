"""Recursion.

Recursion is a function calling itself with a smaller problem.

Run me:
    python 138-recursion/lesson_138_recursion.py
"""

from __future__ import annotations


def factorial(number: int) -> int:
    """Return the product of all numbers up to ``number``.

    Args:
        number: A whole number of 0 or more.

    Returns:
        The factorial.

    Examples:
        >>> factorial(5)
        120
    """
    if number <= 1:
        return 1
    return number * factorial(number - 1)


def total_length(text: str) -> int:
    """Return how many characters a string holds.

    Args:
        text: The string to measure.

    Returns:
        The number of characters.
    """
    if not text:
        return 0
    return len(text[0]) + total_length(text[1:])


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(factorial(5))
    print(total_length("hello"))


if __name__ == "__main__":
    main()
