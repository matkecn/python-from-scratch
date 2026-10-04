"""Tests for Advanced-project-01."""

from lesson_961_advanced_project_01 import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Advanced-project-01' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Advanced-project-01' still holds."""
    assert len(outline().splitlines()) == 3
