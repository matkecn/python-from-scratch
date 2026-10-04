"""Tests for Match."""

from lesson_055_match import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Match' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Match' still holds."""
    assert len(outline().splitlines()) == 3
