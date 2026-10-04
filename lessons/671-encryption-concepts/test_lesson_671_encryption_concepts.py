"""Tests for Encryption-concepts."""

from lesson_671_encryption_concepts import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Encryption-concepts' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Encryption-concepts' still holds."""
    assert len(outline().splitlines()) == 3
