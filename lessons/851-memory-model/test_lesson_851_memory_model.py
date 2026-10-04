"""Tests for Memory-model."""

from lesson_851_memory_model import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Memory-model' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Memory-model' still holds."""
    assert len(outline().splitlines()) == 3
