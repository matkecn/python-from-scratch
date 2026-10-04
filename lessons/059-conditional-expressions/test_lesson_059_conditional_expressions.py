"""Tests for Conditional-expressions."""

from lesson_059_conditional_expressions import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Conditional-expressions' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Conditional-expressions' still holds."""
    assert len(outline().splitlines()) == 3
