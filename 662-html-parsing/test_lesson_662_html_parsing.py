"""Tests for Html-parsing."""

from lesson_662_html_parsing import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Html-parsing' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Html-parsing' still holds."""
    assert len(outline().splitlines()) == 3
