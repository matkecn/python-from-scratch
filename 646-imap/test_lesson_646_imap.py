"""Tests for Imap."""

from lesson_646_imap import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Imap' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Imap' still holds."""
    assert len(outline().splitlines()) == 3
