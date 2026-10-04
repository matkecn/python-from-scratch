"""Tests for Async-iterators."""

from lesson_832_async_iterators import double, double_all


import asyncio


def test_doubles_all() -> None:
    """The promise of lesson 'Async-iterators' still holds."""
    assert asyncio.run(double_all([1, 2])) == [2, 4]
