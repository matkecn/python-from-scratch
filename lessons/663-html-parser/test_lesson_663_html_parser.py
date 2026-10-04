"""Tests for Html-parser."""

from lesson_663_html_parser import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Html-parser' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Html-parser' still holds."""
    assert len(outline().splitlines()) == 3
