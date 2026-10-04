"""Tests for Type-hints."""

from lesson_351_type_hints import double, average


def test_doubles() -> None:
    """The promise of lesson 'Type-hints' still holds."""
    assert double(4) == 8


def test_averages() -> None:
    """The promise of lesson 'Type-hints' still holds."""
    assert average([1.0, 3.0]) == 2.0
