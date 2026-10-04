"""Tests for Debugging-challenges."""

from lesson_982_debugging_challenges import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Debugging-challenges' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Debugging-challenges' still holds."""
    assert len(outline().splitlines()) == 3
