"""Tests for Collections-counter."""

from lesson_533_collections_counter import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Collections-counter' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Collections-counter' still holds."""
    assert len(outline().splitlines()) == 3
