"""Tests for Web-app-concepts."""

from lesson_921_web_app_concepts import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Web-app-concepts' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Web-app-concepts' still holds."""
    assert len(outline().splitlines()) == 3
