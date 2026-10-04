"""Tests for Python versions."""

import pytest

from lesson_004_python_versions import compare, needs_upgrade, parse_version


def test_parses_three_numbers() -> None:
    """A full version gives three numbers."""
    assert parse_version("3.12.1") == (3, 12, 1)


def test_missing_patch_becomes_zero() -> None:
    """A short version is padded with zeros."""
    assert parse_version("3.12") == (3, 12, 0)


def test_rejects_nonsense() -> None:
    """Text that is not a version is refused."""
    with pytest.raises(ValueError):
        parse_version("newest")


def test_compares_versions() -> None:
    """Older is minus one, newer is plus one, equal is zero."""
    assert compare("3.11.0", "3.12.0") == -1
    assert compare("3.12.0", "3.12.0") == 0
    assert compare("3.13.0", "3.12.0") == 1


def test_knows_what_is_too_old() -> None:
    """Python 2 and early Python 3 are too old."""
    assert needs_upgrade("3.8.10") is True
    assert needs_upgrade("2.7.18") is True
    assert needs_upgrade("3.13.0") is False
