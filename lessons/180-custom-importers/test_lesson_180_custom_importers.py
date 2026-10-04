"""Tests for Custom-importers."""

from lesson_180_custom_importers import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Custom-importers' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Custom-importers' still holds."""
    assert len(outline().splitlines()) == 3
