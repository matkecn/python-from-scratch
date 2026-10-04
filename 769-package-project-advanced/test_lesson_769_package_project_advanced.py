"""Tests for Package-project-advanced."""

from lesson_769_package_project_advanced import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Package-project-advanced' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Package-project-advanced' still holds."""
    assert len(outline().splitlines()) == 3
