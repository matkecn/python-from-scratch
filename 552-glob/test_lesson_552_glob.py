"""Tests for Glob."""

from lesson_552_glob import module_path, public_names


def test_has_a_path() -> None:
    """The promise of lesson 'Glob' still holds."""
    assert isinstance(module_path(), str)


def test_lists_names() -> None:
    """The promise of lesson 'Glob' still holds."""
    assert isinstance(public_names(), list)
