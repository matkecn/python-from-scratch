"""Tests for Cli-weather."""

from lesson_907_cli_weather import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Cli-weather' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Cli-weather' still holds."""
    assert len(outline().splitlines()) == 3
