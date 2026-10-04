"""Tests for Api-debugging."""

from lesson_697_api_debugging import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Api-debugging' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Api-debugging' still holds."""
    assert len(outline().splitlines()) == 3
