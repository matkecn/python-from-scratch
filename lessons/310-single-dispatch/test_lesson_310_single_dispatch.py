"""Tests for Single-dispatch."""

from lesson_310_single_dispatch import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Single-dispatch' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Single-dispatch' still holds."""
    assert len(outline().splitlines()) == 3
