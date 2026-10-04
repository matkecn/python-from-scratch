"""Tests for Response-headers."""

from lesson_616_response_headers import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Response-headers' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Response-headers' still holds."""
    assert len(outline().splitlines()) == 3
