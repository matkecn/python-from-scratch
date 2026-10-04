"""Tests for Yield-from."""

from lesson_258_yield_from import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Yield-from' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Yield-from' still holds."""
    assert len(outline().splitlines()) == 3
