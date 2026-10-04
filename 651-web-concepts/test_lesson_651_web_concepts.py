"""Tests for Web-concepts."""

from lesson_651_web_concepts import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Web-concepts' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Web-concepts' still holds."""
    assert len(outline().splitlines()) == 3
