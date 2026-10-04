"""Tests for Github-actions."""

from lesson_786_github_actions import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Github-actions' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Github-actions' still holds."""
    assert len(outline().splitlines()) == 3
