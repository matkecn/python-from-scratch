"""Tests for Cli-log-analyzer."""

from lesson_910_cli_log_analyzer import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Cli-log-analyzer' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Cli-log-analyzer' still holds."""
    assert len(outline().splitlines()) == 3
