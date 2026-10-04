"""Tests for Async-iterator."""

from lesson_439_async_iterator import double, double_all


import asyncio


def test_doubles_all() -> None:
    """The promise of lesson 'Async-iterator' still holds."""
    assert asyncio.run(double_all([1, 2])) == [2, 4]
