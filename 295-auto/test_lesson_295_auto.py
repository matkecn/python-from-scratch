"""Tests for Auto."""

from lesson_295_auto import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Auto' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Auto' still holds."""
    assert len(outline().splitlines()) == 3
