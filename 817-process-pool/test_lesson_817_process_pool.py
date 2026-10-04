"""Tests for Process-pool."""

from lesson_817_process_pool import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Process-pool' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Process-pool' still holds."""
    assert len(outline().splitlines()) == 3
