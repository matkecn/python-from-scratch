"""Tests for Collections-deque."""

from lesson_534_collections_deque import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Collections-deque' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Collections-deque' still holds."""
    assert len(outline().splitlines()) == 3
