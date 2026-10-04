"""Test-driven-development.

Tests are code that checks your code still works.

Run me:
    python 734-test-driven-development/lesson_734_test_driven_development.py
"""

from __future__ import annotations


def add(first: int, second: int) -> int:
    """Add two numbers.

    Args:
        first: The first number.
        second: The second number.

    Returns:
        The total.
    """
    return first + second


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(add(2, 3))


if __name__ == "__main__":
    main()
