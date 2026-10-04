"""Tests for Asyncio."""

from lesson_821_asyncio import module_path, public_names


def test_has_a_path() -> None:
    """The promise of lesson 'Asyncio' still holds."""
    assert isinstance(module_path(), str)


def test_lists_names() -> None:
    """The promise of lesson 'Asyncio' still holds."""
    assert isinstance(public_names(), list)
