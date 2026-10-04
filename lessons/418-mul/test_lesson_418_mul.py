"""Tests for Mul."""

from lesson_418_mul import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Mul' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Mul' still holds."""
    assert len(outline().splitlines()) == 3
