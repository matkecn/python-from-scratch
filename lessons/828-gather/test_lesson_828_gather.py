"""Tests for Gather."""

from lesson_828_gather import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Gather' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Gather' still holds."""
    assert len(outline().splitlines()) == 3
