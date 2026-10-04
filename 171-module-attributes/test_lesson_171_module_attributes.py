"""Tests for Module-attributes."""

from lesson_171_module_attributes import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Module-attributes' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Module-attributes' still holds."""
    assert len(outline().splitlines()) == 3
