"""Tests for Pagination-scraping."""

from lesson_667_pagination_scraping import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Pagination-scraping' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Pagination-scraping' still holds."""
    assert len(outline().splitlines()) == 3
