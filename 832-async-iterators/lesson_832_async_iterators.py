"""Async-iterators.

`async` lets one program wait for many slow things at once.

Run me:
    python 832-async-iterators/lesson_832_async_iterators.py
"""

from __future__ import annotations


import asyncio


async def double(number: int) -> int:
    """Double a number after a tiny pause.

    Args:
        number: The number to double.

    Returns:
        The doubled number.
    """
    await asyncio.sleep(0)
    return number * 2


async def double_all(numbers: list[int]) -> list[int]:
    """Double many numbers at the same time.

    Args:
        numbers: The numbers to double.

    Returns:
        The doubled numbers, in order.
    """
    return list(await asyncio.gather(*(double(number) for number in numbers)))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    import asyncio

    print(asyncio.run(double_all([1, 2, 3])))


if __name__ == "__main__":
    main()
