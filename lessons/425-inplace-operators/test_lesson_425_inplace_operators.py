"""Tests for Inplace-operators."""

from lesson_425_inplace_operators import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Inplace-operators' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Inplace-operators' still holds."""
    assert len(outline().splitlines()) == 3
