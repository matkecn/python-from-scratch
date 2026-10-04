"""Tests for Async-tasks."""

from lesson_826_async_tasks import double, double_all


import asyncio


def test_doubles_all() -> None:
    """The promise of lesson 'Async-tasks' still holds."""
    assert asyncio.run(double_all([1, 2])) == [2, 4]
