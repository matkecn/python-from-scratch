"""Tests for Single-inheritance."""

from lesson_214_single_inheritance import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Single-inheritance' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Single-inheritance' still holds."""
    assert len(outline().splitlines()) == 3
