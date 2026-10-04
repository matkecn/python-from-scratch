"""Tests for Final-python-capstone."""

from lesson_999_final_python_capstone import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Final-python-capstone' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Final-python-capstone' still holds."""
    assert len(outline().splitlines()) == 3
