"""Tests for Sets."""

from lesson_087_sets import unique_letters, shared


def test_drops_repeats() -> None:
    """The promise of lesson 'Sets' still holds."""
    assert unique_letters("aab") == {"a", "b"}


def test_finds_common() -> None:
    """The promise of lesson 'Sets' still holds."""
    assert shared({"a", "b"}, {"b"}) == {"b"}
