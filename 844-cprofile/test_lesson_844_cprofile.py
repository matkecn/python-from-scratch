"""Tests for Cprofile."""

from lesson_844_cprofile import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Cprofile' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Cprofile' still holds."""
    assert len(outline().splitlines()) == 3
