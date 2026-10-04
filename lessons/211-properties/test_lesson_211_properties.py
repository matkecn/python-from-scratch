"""Tests for Properties."""

from lesson_211_properties import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Properties' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Properties' still holds."""
    assert len(outline().splitlines()) == 3
