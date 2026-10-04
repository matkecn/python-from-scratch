"""Tests for Interpreter."""

from lesson_891_interpreter import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Interpreter' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Interpreter' still holds."""
    assert len(outline().splitlines()) == 3
