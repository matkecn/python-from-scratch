"""Tests for String interning."""

from lesson_859_string_interning import shout, count_words, initials


def test_upper_cases() -> None:
    """The promise of lesson 'String interning' still holds."""
    assert shout("hello") == "HELLO"


def test_counts_words() -> None:
    """The promise of lesson 'String interning' still holds."""
    assert count_words("a b c") == 3


def test_makes_initials() -> None:
    """The promise of lesson 'String interning' still holds."""
    assert initials("Ada Lovelace") == "AL"
