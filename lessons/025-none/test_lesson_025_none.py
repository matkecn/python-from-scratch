"""Tests for None."""

from lesson_025_none import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'None' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'None' still holds."""
    assert len(outline().splitlines()) == 3
