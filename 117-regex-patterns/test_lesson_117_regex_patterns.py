"""Tests for Regex-patterns."""

from lesson_117_regex_patterns import find_digits, is_valid_pin


def test_finds_digits() -> None:
    """The promise of lesson 'Regex-patterns' still holds."""
    assert find_digits("a1 b22") == ["1", "22"]


def test_checks_pin() -> None:
    """The promise of lesson 'Regex-patterns' still holds."""
    assert is_valid_pin("1234") is True
