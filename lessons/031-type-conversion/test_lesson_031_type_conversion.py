"""Tests for Type-conversion."""

from lesson_031_type_conversion import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Type-conversion' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Type-conversion' still holds."""
    assert len(outline().splitlines()) == 3
