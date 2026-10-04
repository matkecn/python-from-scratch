"""Tests for Unary-operators."""

from lesson_049_unary_operators import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Unary-operators' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Unary-operators' still holds."""
    assert len(outline().splitlines()) == 3
