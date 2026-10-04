"""Tests for Hmac."""

from lesson_562_hmac import module_path, public_names


def test_has_a_path() -> None:
    """The promise of lesson 'Hmac' still holds."""
    assert isinstance(module_path(), str)


def test_lists_names() -> None:
    """The promise of lesson 'Hmac' still holds."""
    assert isinstance(public_names(), list)
