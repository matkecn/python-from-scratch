"""Tests for Raise."""

from lesson_186_raise import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Raise' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Raise' still holds."""
    assert len(outline().splitlines()) == 3
