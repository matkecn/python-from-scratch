"""Tests for Async-protocol."""

from lesson_437_async_protocol import double, double_all


import asyncio


def test_doubles_all() -> None:
    """The promise of lesson 'Async-protocol' still holds."""
    assert asyncio.run(double_all([1, 2])) == [2, 4]
