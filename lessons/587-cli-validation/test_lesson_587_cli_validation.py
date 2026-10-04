"""Tests for Cli-validation."""

from lesson_587_cli_validation import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Cli-validation' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Cli-validation' still holds."""
    assert len(outline().splitlines()) == 3
