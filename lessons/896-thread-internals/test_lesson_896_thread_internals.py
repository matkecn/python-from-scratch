"""Tests for Thread-internals."""

from lesson_896_thread_internals import double, double_all


def test_doubles_with_threads() -> None:
    """The promise of lesson 'Thread-internals' still holds."""
    assert double_all([1, 2, 3]) == [2, 4, 6]
