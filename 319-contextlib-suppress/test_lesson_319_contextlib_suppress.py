"""Tests for Contextlib-suppress."""

from lesson_319_contextlib_suppress import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Contextlib-suppress' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Contextlib-suppress' still holds."""
    assert len(outline().splitlines()) == 3
