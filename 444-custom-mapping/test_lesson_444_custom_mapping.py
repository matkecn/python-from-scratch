"""Tests for Custom-mapping."""

from lesson_444_custom_mapping import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Custom-mapping' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Custom-mapping' still holds."""
    assert len(outline().splitlines()) == 3
