"""Generic-functions.

A function is a named recipe you can run again and again.

Run me:
    python 366-generic-functions/lesson_366_generic_functions.py
"""

from __future__ import annotations


def area(width: float, height: float) -> float:
    """Return the area of a rectangle.

    Args:
        width: How wide it is.
        height: How tall it is.

    Returns:
        The area.

    Examples:
        >>> area(2.0, 3.0)
        6.0
    """
    return width * height


def describe(width: float, height: float) -> str:
    """Describe a rectangle in words.

    Args:
        width: How wide it is.
        height: How tall it is.

    Returns:
        A short sentence.
    """
    return f"A rectangle of {area(width, height)} square units."


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(area(2.0, 3.0))
    print(describe(2.0, 3.0))


if __name__ == "__main__":
    main()
