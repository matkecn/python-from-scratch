"""Tests for Archive-project."""

from lesson_576_archive_project import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Archive-project' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Archive-project' still holds."""
    assert len(outline().splitlines()) == 3
