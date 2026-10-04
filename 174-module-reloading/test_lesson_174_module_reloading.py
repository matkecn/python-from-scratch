"""Tests for Module-reloading."""

from lesson_174_module_reloading import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Module-reloading' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Module-reloading' still holds."""
    assert len(outline().splitlines()) == 3
