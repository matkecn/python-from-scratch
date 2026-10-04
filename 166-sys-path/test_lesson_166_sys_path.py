"""Tests for Sys-path."""

from lesson_166_sys_path import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Sys-path' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Sys-path' still holds."""
    assert len(outline().splitlines()) == 3
