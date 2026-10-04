"""Tests for Property-testing."""

from lesson_732_property_testing import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Property-testing' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Property-testing' still holds."""
    assert len(outline().splitlines()) == 3
