"""Tests for Build-your-own-web-api."""

from lesson_993_build_your_own_web_api import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Build-your-own-web-api' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Build-your-own-web-api' still holds."""
    assert len(outline().splitlines()) == 3
