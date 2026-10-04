"""Tests for __bytes__."""

from lesson_405_bytes import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson '__bytes__' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson '__bytes__' still holds."""
    assert len(outline().splitlines()) == 3
