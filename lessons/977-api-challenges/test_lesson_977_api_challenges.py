"""Tests for Api-challenges."""

from lesson_977_api_challenges import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Api-challenges' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Api-challenges' still holds."""
    assert len(outline().splitlines()) == 3
