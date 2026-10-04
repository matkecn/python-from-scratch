"""Tests for Assert."""

from lesson_193_assert import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Assert' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Assert' still holds."""
    assert len(outline().splitlines()) == 3
