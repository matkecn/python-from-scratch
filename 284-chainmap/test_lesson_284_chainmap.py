"""Tests for Chainmap."""

from lesson_284_chainmap import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Chainmap' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Chainmap' still holds."""
    assert len(outline().splitlines()) == 3
