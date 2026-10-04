"""Tests for Packages."""

from lesson_167_packages import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Packages' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Packages' still holds."""
    assert len(outline().splitlines()) == 3
