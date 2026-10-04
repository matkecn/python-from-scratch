"""Tests for Cli-calculator."""

from lesson_902_cli_calculator import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Cli-calculator' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Cli-calculator' still holds."""
    assert len(outline().splitlines()) == 3
