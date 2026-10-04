"""Tests for Getattribute."""

from lesson_333_getattribute import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Getattribute' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Getattribute' still holds."""
    assert len(outline().splitlines()) == 3
