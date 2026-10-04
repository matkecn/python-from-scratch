"""Tests for Set-up-tear-down."""

from lesson_715_set_up_tear_down import unique_letters, shared


def test_drops_repeats() -> None:
    """The promise of lesson 'Set-up-tear-down' still holds."""
    assert unique_letters("aab") == {"a", "b"}


def test_finds_common() -> None:
    """The promise of lesson 'Set-up-tear-down' still holds."""
    assert shared({"a", "b"}, {"b"}) == {"b"}
