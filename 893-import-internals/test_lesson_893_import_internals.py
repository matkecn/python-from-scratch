"""Tests for Import-internals."""

from lesson_893_import_internals import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Import-internals' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Import-internals' still holds."""
    assert len(outline().splitlines()) == 3
