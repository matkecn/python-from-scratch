"""Tests for Getopt."""

from lesson_582_getopt import module_path, public_names


def test_has_a_path() -> None:
    """The promise of lesson 'Getopt' still holds."""
    assert isinstance(module_path(), str)


def test_lists_names() -> None:
    """The promise of lesson 'Getopt' still holds."""
    assert isinstance(public_names(), list)
