"""Tests for Args."""

from lesson_128_args import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Args' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Args' still holds."""
    assert len(outline().splitlines()) == 3
