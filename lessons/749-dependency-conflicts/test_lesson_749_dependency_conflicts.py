"""Tests for Dependency-conflicts."""

from lesson_749_dependency_conflicts import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Dependency-conflicts' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Dependency-conflicts' still holds."""
    assert len(outline().splitlines()) == 3
