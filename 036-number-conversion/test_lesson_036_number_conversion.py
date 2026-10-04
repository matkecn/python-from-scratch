"""Tests for Number-conversion."""

from lesson_036_number_conversion import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Number-conversion' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Number-conversion' still holds."""
    assert len(outline().splitlines()) == 3
