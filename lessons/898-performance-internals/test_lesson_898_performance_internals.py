"""Tests for Performance-internals."""

from lesson_898_performance_internals import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Performance-internals' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Performance-internals' still holds."""
    assert len(outline().splitlines()) == 3
