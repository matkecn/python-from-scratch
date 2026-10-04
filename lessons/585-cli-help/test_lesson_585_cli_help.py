"""Tests for Cli-help."""

from lesson_585_cli_help import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Cli-help' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Cli-help' still holds."""
    assert len(outline().splitlines()) == 3
