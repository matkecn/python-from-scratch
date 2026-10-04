"""Tests for Web-framework-concepts."""

from lesson_924_web_framework_concepts import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Web-framework-concepts' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Web-framework-concepts' still holds."""
    assert len(outline().splitlines()) == 3
