"""Tests for Processes."""

from lesson_802_processes import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Processes' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Processes' still holds."""
    assert len(outline().splitlines()) == 3
