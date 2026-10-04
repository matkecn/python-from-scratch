"""Tests for Scheduled-scripts."""

from lesson_946_scheduled_scripts import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Scheduled-scripts' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Scheduled-scripts' still holds."""
    assert len(outline().splitlines()) == 3
