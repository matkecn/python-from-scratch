"""Tests for Create-task."""

from lesson_827_create_task import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Create-task' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Create-task' still holds."""
    assert len(outline().splitlines()) == 3
