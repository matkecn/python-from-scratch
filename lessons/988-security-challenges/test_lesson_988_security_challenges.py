"""Tests for Security-challenges."""

from lesson_988_security_challenges import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Security-challenges' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Security-challenges' still holds."""
    assert len(outline().splitlines()) == 3
