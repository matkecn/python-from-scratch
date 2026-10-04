"""Tests for Name-resolution."""

from lesson_157_name_resolution import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Name-resolution' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Name-resolution' still holds."""
    assert len(outline().splitlines()) == 3
