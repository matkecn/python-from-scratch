"""Tests for Enum."""

from lesson_292_enum import module_path, public_names


def test_has_a_path() -> None:
    """The promise of lesson 'Enum' still holds."""
    assert isinstance(module_path(), str)


def test_lists_names() -> None:
    """The promise of lesson 'Enum' still holds."""
    assert isinstance(public_names(), list)
