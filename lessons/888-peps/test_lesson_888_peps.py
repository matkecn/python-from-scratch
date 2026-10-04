"""Tests for Peps."""

from lesson_888_peps import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Peps' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Peps' still holds."""
    assert len(outline().splitlines()) == 3
