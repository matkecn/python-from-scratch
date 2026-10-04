"""Tuple-slicing.

A tuple is a list that cannot be changed.

Run me:
    python 083-tuple-slicing/lesson_083_tuple_slicing.py
"""

from __future__ import annotations


def first_and_last(numbers: tuple[int, ...]) -> tuple[int, int]:
    """Return the first and last number of a tuple.

    Args:
        numbers: A tuple with at least one number.

    Returns:
        The first and last number.

    Raises:
        ValueError: If the tuple is empty.

    Examples:
        >>> first_and_last((3, 4, 5))
        (3, 5)
    """
    if not numbers:
        raise ValueError("tuple is empty")
    return numbers[0], numbers[-1]


def swap(pair: tuple[int, int]) -> tuple[int, int]:
    """Swap the two numbers in a pair.

    Args:
        pair: Two numbers.

    Returns:
        The pair, backwards.

    Examples:
        >>> swap((1, 2))
        (2, 1)
    """
    left, right = pair
    return right, left


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(first_and_last((3, 4, 5)))
    print(swap((1, 2)))


if __name__ == "__main__":
    main()
