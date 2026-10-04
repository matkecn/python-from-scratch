"""Tests for Exception-practice."""

from lesson_200_exception_practice import parse_age

import pytest


def test_reads_a_number() -> None:
    """The promise of lesson 'Exception-practice' still holds."""
    assert parse_age("12") == 12


def test_rejects_text() -> None:
    """The promise of lesson 'Exception-practice' still holds."""
    with pytest.raises(ValueError):
        parse_age("old")
