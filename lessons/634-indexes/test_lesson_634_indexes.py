"""Tests for Indexes."""

from lesson_634_indexes import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Indexes' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Indexes' still holds."""
    assert len(outline().splitlines()) == 3
