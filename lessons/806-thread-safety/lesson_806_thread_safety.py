"""Thread-safety.

Threads run many tasks at once inside one program.

Run me:
    python 806-thread-safety/lesson_806_thread_safety.py
"""

from __future__ import annotations


from concurrent.futures import ThreadPoolExecutor


def double(number: int) -> int:
    """Double a number.

    Args:
        number: The number to double.

    Returns:
        The doubled number.
    """
    return number * 2


def double_all(numbers: list[int]) -> list[int]:
    """Double many numbers using a pool of threads.

    Args:
        numbers: The numbers to double.

    Returns:
        The doubled numbers, in order.
    """
    with ThreadPoolExecutor(max_workers=4) as pool:
        return list(pool.map(double, numbers))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(double_all([1, 2, 3]))


if __name__ == "__main__":
    main()
