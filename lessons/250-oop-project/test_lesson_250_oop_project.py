"""Tests for Oop-project."""

from lesson_250_oop_project import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Oop-project' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Oop-project' still holds."""
    assert len(outline().splitlines()) == 3
