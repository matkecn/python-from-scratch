"""Tests for Threading-project."""

from lesson_815_threading_project import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Threading-project' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Threading-project' still holds."""
    assert len(outline().splitlines()) == 3
