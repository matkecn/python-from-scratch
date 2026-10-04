"""Tests for Rate-limiting."""

from lesson_666_rate_limiting import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Rate-limiting' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Rate-limiting' still holds."""
    assert len(outline().splitlines()) == 3
