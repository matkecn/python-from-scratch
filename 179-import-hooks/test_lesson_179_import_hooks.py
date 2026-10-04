"""Tests for Import-hooks."""

from lesson_179_import_hooks import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Import-hooks' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Import-hooks' still holds."""
    assert len(outline().splitlines()) == 3
