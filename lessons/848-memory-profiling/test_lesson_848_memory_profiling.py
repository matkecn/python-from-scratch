"""Tests for Memory-profiling."""

from lesson_848_memory_profiling import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Memory-profiling' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Memory-profiling' still holds."""
    assert len(outline().splitlines()) == 3
