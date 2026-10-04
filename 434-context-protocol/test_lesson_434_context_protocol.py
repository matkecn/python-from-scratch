"""Tests for Context-protocol."""

from lesson_434_context_protocol import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Context-protocol' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Context-protocol' still holds."""
    assert len(outline().splitlines()) == 3
