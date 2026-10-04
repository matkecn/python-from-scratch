"""Tests for Intermediate-project-05."""

from lesson_960_intermediate_project_05 import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Intermediate-project-05' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Intermediate-project-05' still holds."""
    assert len(outline().splitlines()) == 3
