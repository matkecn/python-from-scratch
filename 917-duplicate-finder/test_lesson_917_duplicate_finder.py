"""Tests for Duplicate-finder."""

from lesson_917_duplicate_finder import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Duplicate-finder' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Duplicate-finder' still holds."""
    assert len(outline().splitlines()) == 3
