"""Tests for Cli-output."""

from lesson_588_cli_output import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Cli-output' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Cli-output' still holds."""
    assert len(outline().splitlines()) == 3
