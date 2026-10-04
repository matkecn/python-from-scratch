"""Tests for Collections-userstring."""

from lesson_539_collections_userstring import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Collections-userstring' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Collections-userstring' still holds."""
    assert len(outline().splitlines()) == 3
