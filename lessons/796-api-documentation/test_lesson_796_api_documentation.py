"""Tests for Api-documentation."""

from lesson_796_api_documentation import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Api-documentation' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Api-documentation' still holds."""
    assert len(outline().splitlines()) == 3
