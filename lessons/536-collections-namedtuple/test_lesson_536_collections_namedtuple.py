"""Tests for Collections-namedtuple."""

from lesson_536_collections_namedtuple import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Collections-namedtuple' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Collections-namedtuple' still holds."""
    assert len(outline().splitlines()) == 3
