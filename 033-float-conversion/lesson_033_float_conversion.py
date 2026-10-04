"""Float-conversion.

Floats are numbers with a decimal point.

Run me:
    python 033-float-conversion/lesson_033_float_conversion.py
"""

from __future__ import annotations


def average(numbers: list[float]) -> float:
    """Return the mean of some numbers.

    Args:
        numbers: The numbers to average. Must not be empty.

    Returns:
        The mean, rounded to two decimal places.

    Raises:
        ValueError: If ``numbers`` is empty.

    Examples:
        >>> average([1.0, 2.0, 4.0])
        2.33
    """
    if not numbers:
        raise ValueError("need at least one number")
    return round(sum(numbers) / len(numbers), 2)


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(average([1.0, 2.0, 4.0]))


if __name__ == "__main__":
    main()
