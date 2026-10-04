"""Tests for Cli-project."""

from lesson_590_cli_project import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Cli-project' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Cli-project' still holds."""
    assert len(outline().splitlines()) == 3
