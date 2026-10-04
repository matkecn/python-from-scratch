"""Tests for Beginner-project-02."""

from lesson_952_beginner_project_02 import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Beginner-project-02' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Beginner-project-02' still holds."""
    assert len(outline().splitlines()) == 3
