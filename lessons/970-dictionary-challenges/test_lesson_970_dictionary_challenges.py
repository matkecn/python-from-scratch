"""Tests for Dictionary-challenges."""

from lesson_970_dictionary_challenges import word_lengths, lookup


def test_counts_words() -> None:
    """The promise of lesson 'Dictionary-challenges' still holds."""
    assert word_lengths("a bb") == {"a": 1, "bb": 2}


def test_missing_is_safe() -> None:
    """The promise of lesson 'Dictionary-challenges' still holds."""
    assert lookup({}, "nobody") == -1
