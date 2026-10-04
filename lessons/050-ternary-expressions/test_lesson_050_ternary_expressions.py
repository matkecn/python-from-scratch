"""Tests for Ternary-expressions."""

from lesson_050_ternary_expressions import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Ternary-expressions' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Ternary-expressions' still holds."""
    assert len(outline().splitlines()) == 3
