"""Tests for Robots."""

from lesson_665_robots import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Robots' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Robots' still holds."""
    assert len(outline().splitlines()) == 3
