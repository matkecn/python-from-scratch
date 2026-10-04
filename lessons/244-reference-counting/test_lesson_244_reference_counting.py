"""Tests for Reference-counting."""

from lesson_244_reference_counting import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Reference-counting' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Reference-counting' still holds."""
    assert len(outline().splitlines()) == 3
