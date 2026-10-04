"""Tests for Itertools."""

from lesson_269_itertools import module_path, public_names


def test_has_a_path() -> None:
    """The promise of lesson 'Itertools' still holds."""
    assert isinstance(module_path(), str)


def test_lists_names() -> None:
    """The promise of lesson 'Itertools' still holds."""
    assert isinstance(public_names(), list)
