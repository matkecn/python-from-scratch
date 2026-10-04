"""Tests for Lambda."""

from lesson_141_lambda import add_tax, by_length


def test_adds_tax() -> None:
    """The promise of lesson 'Lambda' still holds."""
    assert add_tax(10.0) == 12.0


def test_sorts_long_first() -> None:
    """The promise of lesson 'Lambda' still holds."""
    assert by_length(["a", "ccc", "bb"]) == ["ccc", "bb", "a"]
