"""Tests for Static-methods."""

from lesson_208_static_methods import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Static-methods' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Static-methods' still holds."""
    assert len(outline().splitlines()) == 3
