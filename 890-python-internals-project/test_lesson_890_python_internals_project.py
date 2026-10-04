"""Tests for Python internals project."""

from lesson_890_python_internals_project import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Python internals project' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Python internals project' still holds."""
    assert len(outline().splitlines()) == 3
