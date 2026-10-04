"""Tests for Regex-replacement."""

from lesson_119_regex_replacement import find_digits, is_valid_pin


def test_finds_digits() -> None:
    """The promise of lesson 'Regex-replacement' still holds."""
    assert find_digits("a1 b22") == ["1", "22"]


def test_checks_pin() -> None:
    """The promise of lesson 'Regex-replacement' still holds."""
    assert is_valid_pin("1234") is True
