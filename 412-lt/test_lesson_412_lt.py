"""Tests for Lt."""

from lesson_412_lt import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Lt' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Lt' still holds."""
    assert len(outline().splitlines()) == 3
