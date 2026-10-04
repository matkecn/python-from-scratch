"""Tests for Stack-inspection."""

from lesson_704_stack_inspection import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Stack-inspection' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Stack-inspection' still holds."""
    assert len(outline().splitlines()) == 3
