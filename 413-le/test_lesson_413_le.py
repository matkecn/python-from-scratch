"""Tests for Le."""

from lesson_413_le import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Le' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Le' still holds."""
    assert len(outline().splitlines()) == 3
