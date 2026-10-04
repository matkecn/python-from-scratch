"""Tests for Open-source-challenges."""

from lesson_990_open_source_challenges import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Open-source-challenges' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Open-source-challenges' still holds."""
    assert len(outline().splitlines()) == 3
