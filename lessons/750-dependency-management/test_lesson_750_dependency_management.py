"""Tests for Dependency-management."""

from lesson_750_dependency_management import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Dependency-management' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Dependency-management' still holds."""
    assert len(outline().splitlines()) == 3
