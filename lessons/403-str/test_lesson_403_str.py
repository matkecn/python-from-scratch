"""Tests for Str."""

from lesson_403_str import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Str' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Str' still holds."""
    assert len(outline().splitlines()) == 3
