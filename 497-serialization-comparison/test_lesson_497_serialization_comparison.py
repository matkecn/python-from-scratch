"""Tests for Serialization-comparison."""

from lesson_497_serialization_comparison import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Serialization-comparison' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Serialization-comparison' still holds."""
    assert len(outline().splitlines()) == 3
