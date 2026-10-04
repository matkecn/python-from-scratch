"""Tests for Format-specifiers."""

from lesson_106_format_specifiers import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Format-specifiers' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Format-specifiers' still holds."""
    assert len(outline().splitlines()) == 3
