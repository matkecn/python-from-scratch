"""Tests for Api-testing."""

from lesson_689_api_testing import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Api-testing' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Api-testing' still holds."""
    assert len(outline().splitlines()) == 3
