"""Tests for Command-execution."""

from lesson_509_command_execution import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Command-execution' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Command-execution' still holds."""
    assert len(outline().splitlines()) == 3
