"""Tests for Lru-cache."""

from lesson_308_lru_cache import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Lru-cache' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Lru-cache' still holds."""
    assert len(outline().splitlines()) == 3
