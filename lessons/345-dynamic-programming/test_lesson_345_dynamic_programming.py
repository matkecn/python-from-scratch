"""Tests for Dynamic programming."""

from lesson_345_dynamic_programming import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Dynamic programming' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Dynamic programming' still holds."""
    assert len(outline().splitlines()) == 3
