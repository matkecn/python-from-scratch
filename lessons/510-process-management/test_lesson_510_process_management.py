"""Tests for Process-management."""

from lesson_510_process_management import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Process-management' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Process-management' still holds."""
    assert len(outline().splitlines()) == 3
