"""Tests for Get."""

from lesson_324_get import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Get' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Get' still holds."""
    assert len(outline().splitlines()) == 3
