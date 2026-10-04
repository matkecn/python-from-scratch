"""Tests for Http-status-codes."""

from lesson_614_http_status_codes import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Http-status-codes' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Http-status-codes' still holds."""
    assert len(outline().splitlines()) == 3
