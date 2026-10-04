"""Tests for Log-levels."""

from lesson_592_log_levels import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Log-levels' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Log-levels' still holds."""
    assert len(outline().splitlines()) == 3
