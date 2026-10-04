"""Type-hints.

Type hints describe what a function expects and gives back.

Run me:
    python 351-type-hints/lesson_351_type_hints.py
"""

from __future__ import annotations


def double(number: int) -> int:
    """Double a number.

    Args:
        number: The number to double.

    Returns:
        The doubled number.
    """
    return number * 2


def average(numbers: list[float]) -> float:
    """Return the mean of some numbers.

    Args:
        numbers: A non empty list of numbers.

    Returns:
        The mean.
    """
    return sum(numbers) / len(numbers)


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(double(4))
    print(average([1.0, 2.0]))


if __name__ == "__main__":
    main()
