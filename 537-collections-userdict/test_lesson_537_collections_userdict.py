"""Tests for Collections-userdict."""

from lesson_537_collections_userdict import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Collections-userdict' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Collections-userdict' still holds."""
    assert len(outline().splitlines()) == 3
