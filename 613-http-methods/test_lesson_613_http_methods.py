"""Tests for Http-methods."""

from lesson_613_http_methods import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Http-methods' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Http-methods' still holds."""
    assert len(outline().splitlines()) == 3
