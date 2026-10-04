"""Tests for Concurrency."""

from lesson_801_concurrency import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Concurrency' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Concurrency' still holds."""
    assert len(outline().splitlines()) == 3
