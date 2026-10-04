"""Tests for Performance."""

from lesson_841_performance import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Performance' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Performance' still holds."""
    assert len(outline().splitlines()) == 3
