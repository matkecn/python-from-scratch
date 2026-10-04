"""Tests for Advanced-python-project."""

from lesson_350_advanced_python_project import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Advanced-python-project' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Advanced-python-project' still holds."""
    assert len(outline().splitlines()) == 3
