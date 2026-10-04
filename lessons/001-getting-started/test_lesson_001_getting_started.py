"""Tests for Getting started."""

from lesson_001_getting_started import is_supported, version_number, version_text


def test_version_has_two_numbers() -> None:
    """The version comes back as two whole numbers."""
    major, minor = version_number()
    assert isinstance(major, int)
    assert isinstance(minor, int)


def test_supported_matches_the_version() -> None:
    """We agree with ourselves about which versions are new enough."""
    assert is_supported() == (version_number() >= (3, 11))


def test_version_text_starts_with_python() -> None:
    """The friendly line always starts with the word Python."""
    assert version_text().startswith("Python 3")
