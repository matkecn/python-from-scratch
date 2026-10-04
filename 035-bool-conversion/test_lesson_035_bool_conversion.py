"""Tests for Bool-conversion."""

from lesson_035_bool_conversion import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Bool-conversion' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Bool-conversion' still holds."""
    assert len(outline().splitlines()) == 3
