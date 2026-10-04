"""Tests for Mapping-patterns."""

from lesson_393_mapping_patterns import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Mapping-patterns' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Mapping-patterns' still holds."""
    assert len(outline().splitlines()) == 3
