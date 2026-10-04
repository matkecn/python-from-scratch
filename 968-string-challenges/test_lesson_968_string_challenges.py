"""Tests for String-challenges."""

from lesson_968_string_challenges import shout, count_words, initials


def test_upper_cases() -> None:
    """The promise of lesson 'String-challenges' still holds."""
    assert shout("hello") == "HELLO"


def test_counts_words() -> None:
    """The promise of lesson 'String-challenges' still holds."""
    assert count_words("a b c") == 3


def test_makes_initials() -> None:
    """The promise of lesson 'String-challenges' still holds."""
    assert initials("Ada Lovelace") == "AL"
