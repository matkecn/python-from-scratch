"""Tests for Inspection."""

from lesson_347_inspection import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Inspection' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Inspection' still holds."""
    assert len(outline().splitlines()) == 3
