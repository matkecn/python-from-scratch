"""Tests for Pattern matching."""

from lesson_391_pattern_matching import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Pattern matching' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Pattern matching' still holds."""
    assert len(outline().splitlines()) == 3
