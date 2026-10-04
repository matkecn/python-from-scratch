"""Tests for If-main."""

from lesson_173_if_main import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'If-main' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'If-main' still holds."""
    assert len(outline().splitlines()) == 3
