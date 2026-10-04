"""Tests for Request-headers."""

from lesson_615_request_headers import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Request-headers' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Request-headers' still holds."""
    assert len(outline().splitlines()) == 3
