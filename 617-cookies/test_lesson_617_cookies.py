"""Tests for Cookies."""

from lesson_617_cookies import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Cookies' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Cookies' still holds."""
    assert len(outline().splitlines()) == 3
