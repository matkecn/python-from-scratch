"""Tests for Package-security."""

from lesson_768_package_security import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Package-security' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Package-security' still holds."""
    assert len(outline().splitlines()) == 3
