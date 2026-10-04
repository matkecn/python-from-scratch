"""Tests for Except."""

from lesson_183_except import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Except' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Except' still holds."""
    assert len(outline().splitlines()) == 3
