"""Tests for Dictionary-unpacking."""

from lesson_096_dictionary_unpacking import word_lengths, lookup


def test_counts_words() -> None:
    """The promise of lesson 'Dictionary-unpacking' still holds."""
    assert word_lengths("a bb") == {"a": 1, "bb": 2}


def test_missing_is_safe() -> None:
    """The promise of lesson 'Dictionary-unpacking' still holds."""
    assert lookup({}, "nobody") == -1
