"""Tests for Cancel-tasks."""

from lesson_830_cancel_tasks import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Cancel-tasks' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Cancel-tasks' still holds."""
    assert len(outline().splitlines()) == 3
