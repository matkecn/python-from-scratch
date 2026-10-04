"""Tests for Exception chaining."""

from lesson_189_exception_chaining import parse_age

import pytest


def test_reads_a_number() -> None:
    """The promise of lesson 'Exception chaining' still holds."""
    assert parse_age("12") == 12


def test_rejects_text() -> None:
    """The promise of lesson 'Exception chaining' still holds."""
    with pytest.raises(ValueError):
        parse_age("old")
