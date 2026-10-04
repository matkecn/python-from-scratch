"""Tests for Build-your-own-package."""

from lesson_996_build_your_own_package import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Build-your-own-package' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Build-your-own-package' still holds."""
    assert len(outline().splitlines()) == 3
