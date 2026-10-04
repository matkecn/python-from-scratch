"""Tests for Authentication-app."""

from lesson_933_authentication_app import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Authentication-app' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Authentication-app' still holds."""
    assert len(outline().splitlines()) == 3
