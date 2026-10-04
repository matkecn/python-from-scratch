"""Tests for Cli-todo."""

from lesson_903_cli_todo import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Cli-todo' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Cli-todo' still holds."""
    assert len(outline().splitlines()) == 3
