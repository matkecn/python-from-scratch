"""Tests for Bitwise-dunders."""

from lesson_424_bitwise_dunders import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Bitwise-dunders' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Bitwise-dunders' still holds."""
    assert len(outline().splitlines()) == 3
