"""Tests for Email-attachments."""

from lesson_644_email_attachments import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Email-attachments' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Email-attachments' still holds."""
    assert len(outline().splitlines()) == 3
