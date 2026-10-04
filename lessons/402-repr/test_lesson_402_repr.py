"""Tests for Repr."""

from lesson_402_repr import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Repr' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Repr' still holds."""
    assert len(outline().splitlines()) == 3
