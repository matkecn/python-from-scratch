"""Tests for User-management."""

from lesson_934_user_management import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'User-management' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'User-management' still holds."""
    assert len(outline().splitlines()) == 3
