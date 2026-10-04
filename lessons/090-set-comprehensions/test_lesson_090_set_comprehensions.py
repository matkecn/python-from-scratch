"""Tests for Set-comprehensions."""

from lesson_090_set_comprehensions import unique_letters, shared


def test_drops_repeats() -> None:
    """The promise of lesson 'Set-comprehensions' still holds."""
    assert unique_letters("aab") == {"a", "b"}


def test_finds_common() -> None:
    """The promise of lesson 'Set-comprehensions' still holds."""
    assert shared({"a", "b"}, {"b"}) == {"b"}
