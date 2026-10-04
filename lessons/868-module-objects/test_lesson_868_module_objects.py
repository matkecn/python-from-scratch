"""Tests for Module-objects."""

from lesson_868_module_objects import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Module-objects' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Module-objects' still holds."""
    assert len(outline().splitlines()) == 3
