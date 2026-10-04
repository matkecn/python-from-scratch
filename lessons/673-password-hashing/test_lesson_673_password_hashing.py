"""Tests for Password-hashing."""

from lesson_673_password_hashing import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Password-hashing' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Password-hashing' still holds."""
    assert len(outline().splitlines()) == 3
