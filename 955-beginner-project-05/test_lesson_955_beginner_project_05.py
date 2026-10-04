"""Tests for Beginner-project-05."""

from lesson_955_beginner_project_05 import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Beginner-project-05' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Beginner-project-05' still holds."""
    assert len(outline().splitlines()) == 3
