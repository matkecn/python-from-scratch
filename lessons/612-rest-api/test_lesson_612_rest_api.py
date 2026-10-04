"""Tests for Rest-api."""

from lesson_612_rest_api import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Rest-api' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Rest-api' still holds."""
    assert len(outline().splitlines()) == 3
