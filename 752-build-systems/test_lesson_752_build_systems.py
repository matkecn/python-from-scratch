"""Tests for Build-systems."""

from lesson_752_build_systems import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Build-systems' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Build-systems' still holds."""
    assert len(outline().splitlines()) == 3
