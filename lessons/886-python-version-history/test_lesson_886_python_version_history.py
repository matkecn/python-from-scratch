"""Tests for Python-version-history."""

from lesson_886_python_version_history import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Python-version-history' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Python-version-history' still holds."""
    assert len(outline().splitlines()) == 3
