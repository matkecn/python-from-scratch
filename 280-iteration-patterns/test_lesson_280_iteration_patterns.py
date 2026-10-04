"""Tests for Iteration-patterns."""

from lesson_280_iteration_patterns import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Iteration-patterns' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Iteration-patterns' still holds."""
    assert len(outline().splitlines()) == 3
