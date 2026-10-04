"""Tests for Event loop."""

from lesson_822_event_loop import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Event loop' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Event loop' still holds."""
    assert len(outline().splitlines()) == 3
