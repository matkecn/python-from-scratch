"""Tests for Wsgi."""

from lesson_922_wsgi import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Wsgi' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Wsgi' still holds."""
    assert len(outline().splitlines()) == 3
