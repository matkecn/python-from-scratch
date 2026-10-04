"""Tests for Rest-service."""

from lesson_935_rest_service import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Rest-service' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Rest-service' still holds."""
    assert len(outline().splitlines()) == 3
