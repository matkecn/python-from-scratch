"""Tests for Performance-challenges."""

from lesson_983_performance_challenges import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Performance-challenges' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Performance-challenges' still holds."""
    assert len(outline().splitlines()) == 3
