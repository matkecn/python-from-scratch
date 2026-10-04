"""Tests for Dictionary-indexing."""

from lesson_092_dictionary_indexing import word_lengths, lookup


def test_counts_words() -> None:
    """The promise of lesson 'Dictionary-indexing' still holds."""
    assert word_lengths("a bb") == {"a": 1, "bb": 2}


def test_missing_is_safe() -> None:
    """The promise of lesson 'Dictionary-indexing' still holds."""
    assert lookup({}, "nobody") == -1
