"""Tests for Custom-container."""

from lesson_443_custom_container import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Custom-container' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Custom-container' still holds."""
    assert len(outline().splitlines()) == 3
