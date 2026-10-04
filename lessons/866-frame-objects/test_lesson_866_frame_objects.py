"""Tests for Frame-objects."""

from lesson_866_frame_objects import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Frame-objects' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Frame-objects' still holds."""
    assert len(outline().splitlines()) == 3
