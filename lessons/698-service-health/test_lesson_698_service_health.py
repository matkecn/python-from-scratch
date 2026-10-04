"""Tests for Service-health."""

from lesson_698_service_health import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Service-health' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Service-health' still holds."""
    assert len(outline().splitlines()) == 3
