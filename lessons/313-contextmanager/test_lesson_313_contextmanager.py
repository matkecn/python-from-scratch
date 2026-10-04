"""Tests for Contextmanager."""

from lesson_313_contextmanager import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Contextmanager' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Contextmanager' still holds."""
    assert len(outline().splitlines()) == 3
