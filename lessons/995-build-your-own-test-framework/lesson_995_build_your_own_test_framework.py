"""Build-your-own-test-framework.

Tests are code that checks your code still works.

Run me:
    python 995-build-your-own-test-framework/lesson_995_build_your_own_test_framework.py
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
