"""Tests for Rate-limits."""

from lesson_686_rate_limits import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Rate-limits' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Rate-limits' still holds."""
    assert len(outline().splitlines()) == 3
