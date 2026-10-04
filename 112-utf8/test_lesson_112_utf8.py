"""Tests for UTF-8."""

from lesson_112_utf8 import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'UTF-8' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'UTF-8' still holds."""
    assert len(outline().splitlines()) == 3
