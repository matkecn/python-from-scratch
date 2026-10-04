"""Tests for Async-internals."""

from lesson_897_async_internals import double, double_all


import asyncio


def test_doubles_all() -> None:
    """The promise of lesson 'Async-internals' still holds."""
    assert asyncio.run(double_all([1, 2])) == [2, 4]
