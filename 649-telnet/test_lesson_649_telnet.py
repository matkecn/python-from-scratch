"""Tests for Telnet."""

from lesson_649_telnet import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Telnet' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Telnet' still holds."""
    assert len(outline().splitlines()) == 3
