"""Tests for Timezone."""

from lesson_525_timezone import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Timezone' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Timezone' still holds."""
    assert len(outline().splitlines()) == 3
