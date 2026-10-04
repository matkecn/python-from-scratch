"""Tests for Cors."""

from lesson_660_cors import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Cors' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Cors' still holds."""
    assert len(outline().splitlines()) == 3
