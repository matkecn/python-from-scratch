"""Tests for With-open."""

from lesson_465_with_open import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'With-open' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'With-open' still holds."""
    assert len(outline().splitlines()) == 3
