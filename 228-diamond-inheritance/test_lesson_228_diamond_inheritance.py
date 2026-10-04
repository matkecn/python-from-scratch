"""Tests for Diamond-inheritance."""

from lesson_228_diamond_inheritance import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Diamond-inheritance' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Diamond-inheritance' still holds."""
    assert len(outline().splitlines()) == 3
