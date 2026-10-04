"""Tests for Numbers."""

from lesson_518_numbers import module_path, public_names


def test_has_a_path() -> None:
    """The promise of lesson 'Numbers' still holds."""
    assert isinstance(module_path(), str)


def test_lists_names() -> None:
    """The promise of lesson 'Numbers' still holds."""
    assert isinstance(public_names(), list)
