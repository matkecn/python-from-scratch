"""Tests for Protocols."""

from lesson_367_protocols import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Protocols' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Protocols' still holds."""
    assert len(outline().splitlines()) == 3
