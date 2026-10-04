"""Tests for Backoff."""

from lesson_685_backoff import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Backoff' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Backoff' still holds."""
    assert len(outline().splitlines()) == 3
