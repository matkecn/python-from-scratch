"""Tests for Contextlib-redirect."""

from lesson_320_contextlib_redirect import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Contextlib-redirect' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Contextlib-redirect' still holds."""
    assert len(outline().splitlines()) == 3
