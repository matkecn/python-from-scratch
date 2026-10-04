"""Tests for Templates."""

from lesson_929_templates import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Templates' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Templates' still holds."""
    assert len(outline().splitlines()) == 3
