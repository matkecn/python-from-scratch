"""Tests for Modules."""

from lesson_161_modules import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Modules' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Modules' still holds."""
    assert len(outline().splitlines()) == 3
