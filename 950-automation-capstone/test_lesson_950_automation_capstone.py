"""Tests for Automation-capstone."""

from lesson_950_automation_capstone import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Automation-capstone' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Automation-capstone' still holds."""
    assert len(outline().splitlines()) == 3
