"""Tests for Escape-sequences."""

from lesson_115_escape_sequences import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Escape-sequences' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Escape-sequences' still holds."""
    assert len(outline().splitlines()) == 3
