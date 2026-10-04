"""Tests for Networking-capstone."""

from lesson_700_networking_capstone import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Networking-capstone' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Networking-capstone' still holds."""
    assert len(outline().splitlines()) == 3
