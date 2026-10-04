"""Tests for Module-loaders."""

from lesson_177_module_loaders import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Module-loaders' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Module-loaders' still holds."""
    assert len(outline().splitlines()) == 3
