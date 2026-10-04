"""Tests for Email-automation."""

from lesson_943_email_automation import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Email-automation' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Email-automation' still holds."""
    assert len(outline().splitlines()) == 3
