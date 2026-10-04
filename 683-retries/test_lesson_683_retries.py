"""Tests for Retries."""

from lesson_683_retries import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Retries' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Retries' still holds."""
    assert len(outline().splitlines()) == 3
