"""Tests for Async-challenges."""

from lesson_980_async_challenges import double, double_all


import asyncio


def test_doubles_all() -> None:
    """The promise of lesson 'Async-challenges' still holds."""
    assert asyncio.run(double_all([1, 2])) == [2, 4]
