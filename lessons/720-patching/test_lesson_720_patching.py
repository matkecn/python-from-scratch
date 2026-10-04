"""Tests for Patching."""

from lesson_720_patching import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Patching' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Patching' still holds."""
    assert len(outline().splitlines()) == 3
