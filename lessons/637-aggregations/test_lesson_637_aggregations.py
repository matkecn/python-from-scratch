"""Tests for Aggregations."""

from lesson_637_aggregations import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Aggregations' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Aggregations' still holds."""
    assert len(outline().splitlines()) == 3
