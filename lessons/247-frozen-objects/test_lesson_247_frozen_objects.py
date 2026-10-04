"""Tests for Frozen-objects."""

from lesson_247_frozen_objects import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Frozen-objects' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Frozen-objects' still holds."""
    assert len(outline().splitlines()) == 3
