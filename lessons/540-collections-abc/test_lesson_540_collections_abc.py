"""Tests for Collections-abc."""

from lesson_540_collections_abc import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Collections-abc' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Collections-abc' still holds."""
    assert len(outline().splitlines()) == 3
