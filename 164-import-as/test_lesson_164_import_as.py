"""Tests for import ... as."""

from lesson_164_import_as import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'import ... as' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'import ... as' still holds."""
    assert len(outline().splitlines()) == 3
