"""Tests for Thread-safety."""

from lesson_806_thread_safety import double, double_all


def test_doubles_with_threads() -> None:
    """The promise of lesson 'Thread-safety' still holds."""
    assert double_all([1, 2, 3]) == [2, 4, 6]
