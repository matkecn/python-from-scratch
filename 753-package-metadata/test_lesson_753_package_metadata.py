"""Tests for Package metadata."""

from lesson_753_package_metadata import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Package metadata' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Package metadata' still holds."""
    assert len(outline().splitlines()) == 3
