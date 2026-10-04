"""Tests for Unbound-local."""

from lesson_159_unbound_local import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Unbound-local' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Unbound-local' still holds."""
    assert len(outline().splitlines()) == 3
