"""Tests for Reraise."""

from lesson_187_reraise import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Reraise' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Reraise' still holds."""
    assert len(outline().splitlines()) == 3
