"""Tests for Api-errors."""

from lesson_688_api_errors import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Api-errors' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Api-errors' still holds."""
    assert len(outline().splitlines()) == 3
