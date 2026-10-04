"""Tests for Beginner-project-03."""

from lesson_953_beginner_project_03 import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Beginner-project-03' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Beginner-project-03' still holds."""
    assert len(outline().splitlines()) == 3
