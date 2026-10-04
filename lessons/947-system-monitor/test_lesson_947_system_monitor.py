"""Tests for System-monitor."""

from lesson_947_system_monitor import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'System-monitor' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'System-monitor' still holds."""
    assert len(outline().splitlines()) == 3
