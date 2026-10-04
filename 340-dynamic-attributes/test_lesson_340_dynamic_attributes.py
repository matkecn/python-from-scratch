"""Tests for Dynamic-attributes."""

from lesson_340_dynamic_attributes import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Dynamic-attributes' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Dynamic-attributes' still holds."""
    assert len(outline().splitlines()) == 3
