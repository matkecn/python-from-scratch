"""Tests for Cli-subcommands."""

from lesson_586_cli_subcommands import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Cli-subcommands' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Cli-subcommands' still holds."""
    assert len(outline().splitlines()) == 3
