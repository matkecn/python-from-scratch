"""Tests for Bz2."""

from lesson_569_bz2 import module_path, public_names


def test_has_a_path() -> None:
    """The promise of lesson 'Bz2' still holds."""
    assert isinstance(module_path(), str)


def test_lists_names() -> None:
    """The promise of lesson 'Bz2' still holds."""
    assert isinstance(public_names(), list)
