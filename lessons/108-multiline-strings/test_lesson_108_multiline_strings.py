"""Tests for Multiline-strings."""

from lesson_108_multiline_strings import shout, count_words, initials


def test_upper_cases() -> None:
    """The promise of lesson 'Multiline-strings' still holds."""
    assert shout("hello") == "HELLO"


def test_counts_words() -> None:
    """The promise of lesson 'Multiline-strings' still holds."""
    assert count_words("a b c") == 3


def test_makes_initials() -> None:
    """The promise of lesson 'Multiline-strings' still holds."""
    assert initials("Ada Lovelace") == "AL"
