"""Tests for Testing-project-advanced."""

from lesson_740_testing_project_advanced import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Testing-project-advanced' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Testing-project-advanced' still holds."""
    assert len(outline().splitlines()) == 3
