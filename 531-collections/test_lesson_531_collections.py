"""Tests for Collections."""

from lesson_531_collections import module_path, public_names


def test_has_a_path() -> None:
    """The promise of lesson 'Collections' still holds."""
    assert isinstance(module_path(), str)


def test_lists_names() -> None:
    """The promise of lesson 'Collections' still holds."""
    assert isinstance(public_names(), list)
