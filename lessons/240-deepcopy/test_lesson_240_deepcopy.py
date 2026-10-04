"""Tests for Deepcopy."""

from lesson_240_deepcopy import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Deepcopy' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Deepcopy' still holds."""
    assert len(outline().splitlines()) == 3
