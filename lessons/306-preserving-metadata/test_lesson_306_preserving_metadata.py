"""Tests for Preserving metadata."""

from lesson_306_preserving_metadata import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Preserving metadata' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Preserving metadata' still holds."""
    assert len(outline().splitlines()) == 3
