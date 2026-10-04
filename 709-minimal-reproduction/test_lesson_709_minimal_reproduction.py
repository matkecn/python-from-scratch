"""Tests for Minimal-reproduction."""

from lesson_709_minimal_reproduction import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Minimal-reproduction' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Minimal-reproduction' still holds."""
    assert len(outline().splitlines()) == 3
