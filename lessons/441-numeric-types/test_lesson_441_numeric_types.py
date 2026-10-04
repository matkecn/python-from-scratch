"""Tests for Numeric-types."""

from lesson_441_numeric_types import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Numeric-types' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Numeric-types' still holds."""
    assert len(outline().splitlines()) == 3
