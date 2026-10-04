"""Tests for String-encoding."""

from lesson_109_string_encoding import shout, count_words, initials


def test_upper_cases() -> None:
    """The promise of lesson 'String-encoding' still holds."""
    assert shout("hello") == "HELLO"


def test_counts_words() -> None:
    """The promise of lesson 'String-encoding' still holds."""
    assert count_words("a b c") == 3


def test_makes_initials() -> None:
    """The promise of lesson 'String-encoding' still holds."""
    assert initials("Ada Lovelace") == "AL"
