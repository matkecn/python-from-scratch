"""Tests for Rest-client."""

from lesson_681_rest_client import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Rest-client' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Rest-client' still holds."""
    assert len(outline().splitlines()) == 3
