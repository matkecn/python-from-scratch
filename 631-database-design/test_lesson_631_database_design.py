"""Tests for Database-design."""

from lesson_631_database_design import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Database-design' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Database-design' still holds."""
    assert len(outline().splitlines()) == 3
