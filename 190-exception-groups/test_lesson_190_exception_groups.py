"""Tests for Exception-groups."""

from lesson_190_exception_groups import parse_age

import pytest


def test_reads_a_number() -> None:
    """The promise of lesson 'Exception-groups' still holds."""
    assert parse_age("12") == 12


def test_rejects_text() -> None:
    """The promise of lesson 'Exception-groups' still holds."""
    with pytest.raises(ValueError):
        parse_age("old")
