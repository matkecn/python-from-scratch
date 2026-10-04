"""Tests for Publishing-packages."""

from lesson_758_publishing_packages import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Publishing-packages' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Publishing-packages' still holds."""
    assert len(outline().splitlines()) == 3
