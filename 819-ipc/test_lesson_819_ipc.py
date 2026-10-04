"""Tests for Ipc."""

from lesson_819_ipc import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Ipc' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Ipc' still holds."""
    assert len(outline().splitlines()) == 3
