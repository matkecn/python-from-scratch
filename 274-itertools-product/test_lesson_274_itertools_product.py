"""Tests for Itertools-product."""

from lesson_274_itertools_product import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Itertools-product' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Itertools-product' still holds."""
    assert len(outline().splitlines()) == 3
