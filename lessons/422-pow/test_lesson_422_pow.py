"""Tests for __pow__."""

from lesson_422_pow import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson '__pow__' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson '__pow__' still holds."""
    assert len(outline().splitlines()) == 3
