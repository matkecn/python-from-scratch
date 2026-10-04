"""Tests for Relative-imports."""

from lesson_169_relative_imports import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Relative-imports' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Relative-imports' still holds."""
    assert len(outline().splitlines()) == 3
