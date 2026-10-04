"""Tests for Readme."""

from lesson_792_readme import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Readme' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Readme' still holds."""
    assert len(outline().splitlines()) == 3
