"""Tests for Cli-apps."""

from lesson_901_cli_apps import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Cli-apps' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Cli-apps' still holds."""
    assert len(outline().splitlines()) == 3
