"""Tests for Python-internals-capstone."""

from lesson_900_python_internals_capstone import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Python-internals-capstone' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Python-internals-capstone' still holds."""
    assert len(outline().splitlines()) == 3
