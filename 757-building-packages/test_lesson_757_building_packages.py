"""Tests for Building-packages."""

from lesson_757_building_packages import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Building-packages' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Building-packages' still holds."""
    assert len(outline().splitlines()) == 3
