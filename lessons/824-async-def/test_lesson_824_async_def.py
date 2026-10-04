"""Tests for Async-def."""

from lesson_824_async_def import double, double_all


import asyncio


def test_doubles_all() -> None:
    """The promise of lesson 'Async-def' still holds."""
    assert asyncio.run(double_all([1, 2])) == [2, 4]
