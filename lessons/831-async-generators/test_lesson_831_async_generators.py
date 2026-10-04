"""Tests for Async-generators."""

from lesson_831_async_generators import double, double_all


import asyncio


def test_doubles_all() -> None:
    """The promise of lesson 'Async-generators' still holds."""
    assert asyncio.run(double_all([1, 2])) == [2, 4]
