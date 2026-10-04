"""Tests for Email-project."""

from lesson_647_email_project import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Email-project' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Email-project' still holds."""
    assert len(outline().splitlines()) == 3
