"""Tests for Api-keys."""

from lesson_676_api_keys import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Api-keys' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Api-keys' still holds."""
    assert len(outline().splitlines()) == 3
