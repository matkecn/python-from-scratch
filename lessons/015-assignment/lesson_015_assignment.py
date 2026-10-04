"""Assignment.

``=`` copies a value into a name. ``==`` asks a question. Mixing them up is the
most common small bug in Python.

Run me:
    python 015-assignment/lesson_015_assignment.py
"""

from __future__ import annotations


def are_equal(first: int, second: int) -> bool:
    """Say whether two numbers match.

    Args:
        first: The number on the left.
        second: The number on the right.

    Returns:
        ``True`` when they are equal.

    Examples:
        >>> are_equal(2, 2)
        True
        >>> are_equal(2, 3)
        False
    """
    return first == second


def add_to_total(total: int, amount: int = 1) -> int:
    """Add to a running total.

    Args:
        total: The total so far.
        amount: How much to add.

    Returns:
        The new total.
    """
    total += amount
    return total


def chain() -> tuple[int, int, int]:
    """Show that one value can wear three names.

    Returns:
        Three copies of the same number.

    Examples:
        >>> chain()
        (7, 7, 7)
    """
    first = second = third = 7
    return first, second, third


def count_down(start: int) -> list[int]:
    """Return the numbers from start down to one.

    Args:
        start: The number to start from.

    Returns:
        The numbers, largest first.

    Examples:
        >>> count_down(3)
        [3, 2, 1]
    """
    numbers = list(range(start, 0, -1))
    return numbers


def main() -> None:
    """Compare, then update."""
    total = 0
    for amount in [5, 3, 2]:
        total = add_to_total(total, amount)
    print(f"total is {total}, equal to 10? {are_equal(total, 10)}")
    print(count_down(3))


if __name__ == "__main__":
    main()
