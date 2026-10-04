"""Tests for Bitwise-operators."""

from lesson_044_bitwise_operators import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Bitwise-operators' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Bitwise-operators' still holds."""
    assert len(outline().splitlines()) == 3
