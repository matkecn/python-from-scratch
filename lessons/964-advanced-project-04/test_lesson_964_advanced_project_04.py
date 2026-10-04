"""Tests for Advanced-project-04."""

from lesson_964_advanced_project_04 import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Advanced-project-04' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Advanced-project-04' still holds."""
    assert len(outline().splitlines()) == 3
