"""Tests for __new__."""

from lesson_236_new import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson '__new__' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson '__new__' still holds."""
    assert len(outline().splitlines()) == 3
