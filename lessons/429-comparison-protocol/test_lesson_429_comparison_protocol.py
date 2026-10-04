"""Tests for Comparison-protocol."""

from lesson_429_comparison_protocol import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Comparison-protocol' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Comparison-protocol' still holds."""
    assert len(outline().splitlines()) == 3
