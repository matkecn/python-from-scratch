"""Tests for Token-auth."""

from lesson_675_token_auth import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Token-auth' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Token-auth' still holds."""
    assert len(outline().splitlines()) == 3
