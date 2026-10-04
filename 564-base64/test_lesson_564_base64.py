"""Tests for Base64."""

from lesson_564_base64 import module_path, public_names


def test_has_a_path() -> None:
    """The promise of lesson 'Base64' still holds."""
    assert isinstance(module_path(), str)


def test_lists_names() -> None:
    """The promise of lesson 'Base64' still holds."""
    assert isinstance(public_names(), list)
