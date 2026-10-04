"""Tests for Module-main."""

from lesson_172_module_main import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Module-main' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Module-main' still holds."""
    assert len(outline().splitlines()) == 3
