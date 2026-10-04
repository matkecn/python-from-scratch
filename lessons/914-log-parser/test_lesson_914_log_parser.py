"""Tests for Log-parser."""

from lesson_914_log_parser import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Log-parser' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Log-parser' still holds."""
    assert len(outline().splitlines()) == 3
