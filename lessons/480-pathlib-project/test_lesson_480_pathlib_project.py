"""Tests for Pathlib-project."""

from lesson_480_pathlib_project import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Pathlib-project' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Pathlib-project' still holds."""
    assert len(outline().splitlines()) == 3
