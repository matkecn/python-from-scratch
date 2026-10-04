"""Tests for Itertools-chain."""

from lesson_270_itertools_chain import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Itertools-chain' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Itertools-chain' still holds."""
    assert len(outline().splitlines()) == 3
