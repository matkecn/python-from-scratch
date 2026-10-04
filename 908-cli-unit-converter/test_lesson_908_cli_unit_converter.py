"""Tests for Cli-unit-converter."""

from lesson_908_cli_unit_converter import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Cli-unit-converter' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Cli-unit-converter' still holds."""
    assert len(outline().splitlines()) == 3
