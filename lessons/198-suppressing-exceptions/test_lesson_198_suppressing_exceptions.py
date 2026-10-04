"""Tests for Suppressing-exceptions."""

from lesson_198_suppressing_exceptions import parse_age

import pytest


def test_reads_a_number() -> None:
    """The promise of lesson 'Suppressing-exceptions' still holds."""
    assert parse_age("12") == 12


def test_rejects_text() -> None:
    """The promise of lesson 'Suppressing-exceptions' still holds."""
    with pytest.raises(ValueError):
        parse_age("old")
