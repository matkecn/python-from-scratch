"""Tests for Collections-chainmap."""

from lesson_535_collections_chainmap import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Collections-chainmap' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Collections-chainmap' still holds."""
    assert len(outline().splitlines()) == 3
