"""Tests for Profile."""

from lesson_845_profile import module_path, public_names


def test_has_a_path() -> None:
    """The promise of lesson 'Profile' still holds."""
    assert isinstance(module_path(), str)


def test_lists_names() -> None:
    """The promise of lesson 'Profile' still holds."""
    assert isinstance(public_names(), list)
