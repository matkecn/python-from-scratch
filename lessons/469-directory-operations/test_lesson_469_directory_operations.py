"""Tests for Directory-operations."""

from lesson_469_directory_operations import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Directory-operations' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Directory-operations' still holds."""
    assert len(outline().splitlines()) == 3
