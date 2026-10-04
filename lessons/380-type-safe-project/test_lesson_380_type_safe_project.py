"""Tests for Type-safe-project."""

from lesson_380_type_safe_project import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Type-safe-project' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Type-safe-project' still holds."""
    assert len(outline().splitlines()) == 3
