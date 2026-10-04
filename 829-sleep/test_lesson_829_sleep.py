"""Tests for Sleep."""

from lesson_829_sleep import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Sleep' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Sleep' still holds."""
    assert len(outline().splitlines()) == 3
