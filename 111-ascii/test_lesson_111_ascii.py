"""Tests for Ascii."""

from lesson_111_ascii import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Ascii' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Ascii' still holds."""
    assert len(outline().splitlines()) == 3
