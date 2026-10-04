"""Tests for Os-path."""

from lesson_502_os_path import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Os-path' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Os-path' still holds."""
    assert len(outline().splitlines()) == 3
