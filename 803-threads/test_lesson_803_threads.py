"""Tests for Threads."""

from lesson_803_threads import double, double_all


def test_doubles_with_threads() -> None:
    """The promise of lesson 'Threads' still holds."""
    assert double_all([1, 2, 3]) == [2, 4, 6]
