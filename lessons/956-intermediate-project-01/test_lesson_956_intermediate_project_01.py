"""Tests for Intermediate-project-01."""

from lesson_956_intermediate_project_01 import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Intermediate-project-01' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Intermediate-project-01' still holds."""
    assert len(outline().splitlines()) == 3
