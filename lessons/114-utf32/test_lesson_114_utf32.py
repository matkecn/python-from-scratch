"""Tests for UTF-32."""

from lesson_114_utf32 import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'UTF-32' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'UTF-32' still holds."""
    assert len(outline().splitlines()) == 3
