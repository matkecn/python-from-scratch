"""Tests for Api-vs-scraping."""

from lesson_670_api_vs_scraping import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Api-vs-scraping' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Api-vs-scraping' still holds."""
    assert len(outline().splitlines()) == 3
