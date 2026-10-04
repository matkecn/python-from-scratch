"""Tests for Advanced-project-03."""

from lesson_963_advanced_project_03 import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Advanced-project-03' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Advanced-project-03' still holds."""
    assert len(outline().splitlines()) == 3
