"""Tests for Typing-modules."""

from lesson_377_typing_modules import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Typing-modules' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Typing-modules' still holds."""
    assert len(outline().splitlines()) == 3
