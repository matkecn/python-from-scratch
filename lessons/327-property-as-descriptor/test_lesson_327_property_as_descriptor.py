"""Tests for Property-as-descriptor."""

from lesson_327_property_as_descriptor import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Property-as-descriptor' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Property-as-descriptor' still holds."""
    assert len(outline().splitlines()) == 3
