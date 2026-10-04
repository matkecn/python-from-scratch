"""Tests for Attribute-lookup."""

from lesson_332_attribute_lookup import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Attribute-lookup' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Attribute-lookup' still holds."""
    assert len(outline().splitlines()) == 3
