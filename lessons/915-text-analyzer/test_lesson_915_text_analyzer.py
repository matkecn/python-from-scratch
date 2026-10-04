"""Tests for Text-analyzer."""

from lesson_915_text_analyzer import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Text-analyzer' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Text-analyzer' still holds."""
    assert len(outline().splitlines()) == 3
