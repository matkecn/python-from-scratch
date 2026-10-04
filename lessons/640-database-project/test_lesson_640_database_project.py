"""Tests for Database-project."""

from lesson_640_database_project import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Database-project' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Database-project' still holds."""
    assert len(outline().splitlines()) == 3
