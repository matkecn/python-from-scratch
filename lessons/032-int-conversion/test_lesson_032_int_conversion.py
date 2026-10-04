"""Tests for Int-conversion."""

from lesson_032_int_conversion import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Int-conversion' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Int-conversion' still holds."""
    assert len(outline().splitlines()) == 3
