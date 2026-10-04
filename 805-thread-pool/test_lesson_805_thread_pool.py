"""Tests for Thread-pool."""

from lesson_805_thread_pool import double, double_all


def test_doubles_with_threads() -> None:
    """The promise of lesson 'Thread-pool' still holds."""
    assert double_all([1, 2, 3]) == [2, 4, 6]
