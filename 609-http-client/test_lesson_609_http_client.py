"""Tests for Http-client."""

from lesson_609_http_client import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Http-client' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Http-client' still holds."""
    assert len(outline().splitlines()) == 3
