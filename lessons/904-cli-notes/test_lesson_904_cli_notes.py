"""Tests for Cli-notes."""

from lesson_904_cli_notes import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Cli-notes' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Cli-notes' still holds."""
    assert len(outline().splitlines()) == 3
