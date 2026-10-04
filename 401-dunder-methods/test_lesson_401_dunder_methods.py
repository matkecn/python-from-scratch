"""Tests for Dunder-methods."""

from lesson_401_dunder_methods import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Dunder-methods' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Dunder-methods' still holds."""
    assert len(outline().splitlines()) == 3
