"""Tests for Instance-attributes."""

from lesson_204_instance_attributes import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Instance-attributes' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Instance-attributes' still holds."""
    assert len(outline().splitlines()) == 3
