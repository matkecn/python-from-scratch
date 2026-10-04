"""Tests for Input-validation."""

from lesson_678_input_validation import clean_answer, ask, ask_number


def test_cleans_an_answer() -> None:
    """The promise of lesson 'Input-validation' still holds."""
    assert clean_answer("name", "name: Ada ") == "Ada"


def test_keeps_empty() -> None:
    """The promise of lesson 'Input-validation' still holds."""
    assert clean_answer("name", "   ") == ""
