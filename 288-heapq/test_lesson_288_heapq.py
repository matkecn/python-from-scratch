"""Tests for Heapq."""

from lesson_288_heapq import module_path, public_names


def test_has_a_path() -> None:
    """The promise of lesson 'Heapq' still holds."""
    assert isinstance(module_path(), str)


def test_lists_names() -> None:
    """The promise of lesson 'Heapq' still holds."""
    assert isinstance(public_names(), list)
