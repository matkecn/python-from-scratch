"""Tests for Sequence-protocol."""

from lesson_431_sequence_protocol import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Sequence-protocol' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Sequence-protocol' still holds."""
    assert len(outline().splitlines()) == 3
