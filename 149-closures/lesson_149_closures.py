"""Closures.

A closure is a function that remembers names from around it.

Run me:
    python 149-closures/lesson_149_closures.py
"""

from __future__ import annotations


from collections.abc import Callable


def make_counter(start: int = 0) -> Callable[[], int]:
    """Make a counter that remembers how often it was called.

    Args:
        start: The number to start from.

    Returns:
        A function that counts 1, 2, 3 and so on from ``start``.

    Examples:
        >>> tick = make_counter()
        >>> tick(), tick()
        (1, 2)
    """
    count = start

    def tick() -> int:
        """Add one and return the new count."""
        nonlocal count
        count += 1
        return count

    return tick


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    tick = make_counter()
    print(tick(), tick(), tick())


if __name__ == "__main__":
    main()
