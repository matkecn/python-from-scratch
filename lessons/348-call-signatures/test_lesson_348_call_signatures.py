"""Tests for Call-signatures."""

from lesson_348_call_signatures import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Call-signatures' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Call-signatures' still holds."""
    assert len(outline().splitlines()) == 3
