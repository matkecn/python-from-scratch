"""Tests for Isinstance."""

from lesson_231_isinstance import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Isinstance' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Isinstance' still holds."""
    assert len(outline().splitlines()) == 3
