"""List-mutation.

A list keeps many values in order.

Run me:
    python 078-list-mutation/lesson_078_list_mutation.py
"""

from __future__ import annotations


def add_up(numbers: list[int]) -> int:
    """Add every number in a list.

    Args:
        numbers: The numbers to add.

    Returns:
        The total.

    Examples:
        >>> add_up([1, 2, 3])
        6
    """
    return sum(numbers)


def biggest(numbers: list[int]) -> int:
    """Return the largest number in a list.

    Args:
        numbers: A list that is not empty.

    Returns:
        The largest number.

    Raises:
        ValueError: If the list is empty.

    Examples:
        >>> biggest([4, 9, 2])
        9
    """
    if not numbers:
        raise ValueError("list is empty")
    return max(numbers)


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(add_up([1, 2, 3]))
    print(biggest([4, 9, 2]))


if __name__ == "__main__":
    main()
