"""Tests for Set-methods."""

from lesson_088_set_methods import unique_letters, shared


def test_drops_repeats() -> None:
    """The promise of lesson 'Set-methods' still holds."""
    assert unique_letters("aab") == {"a", "b"}


def test_finds_common() -> None:
    """The promise of lesson 'Set-methods' still holds."""
    assert shared({"a", "b"}, {"b"}) == {"b"}
