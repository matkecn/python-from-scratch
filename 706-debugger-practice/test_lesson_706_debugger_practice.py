"""Tests for Debugger-practice."""

from lesson_706_debugger_practice import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Debugger-practice' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Debugger-practice' still holds."""
    assert len(outline().splitlines()) == 3
