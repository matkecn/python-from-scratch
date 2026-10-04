"""Tests for Ironpython."""

from lesson_885_ironpython import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Ironpython' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Ironpython' still holds."""
    assert len(outline().splitlines()) == 3
