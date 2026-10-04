"""Tests for Caching."""

from lesson_938_caching import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Caching' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Caching' still holds."""
    assert len(outline().splitlines()) == 3
