"""Tests for Testing-async-code."""

from lesson_737_testing_async_code import double, double_all


import asyncio


def test_doubles_all() -> None:
    """The promise of lesson 'Testing-async-code' still holds."""
    assert asyncio.run(double_all([1, 2])) == [2, 4]
