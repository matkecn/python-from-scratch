"""Tests for Memory-internals."""

from lesson_895_memory_internals import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Memory-internals' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Memory-internals' still holds."""
    assert len(outline().splitlines()) == 3
