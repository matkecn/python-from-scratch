"""Tests for Inheritance."""

from lesson_213_inheritance import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Inheritance' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Inheritance' still holds."""
    assert len(outline().splitlines()) == 3
