"""Tests for Set-operations."""

from lesson_089_set_operations import unique_letters, shared


def test_drops_repeats() -> None:
    """The promise of lesson 'Set-operations' still holds."""
    assert unique_letters("aab") == {"a", "b"}


def test_finds_common() -> None:
    """The promise of lesson 'Set-operations' still holds."""
    assert shared({"a", "b"}, {"b"}) == {"b"}
