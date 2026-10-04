"""Tests for Custom-exceptions."""

from lesson_188_custom_exceptions import parse_age

import pytest


def test_reads_a_number() -> None:
    """The promise of lesson 'Custom-exceptions' still holds."""
    assert parse_age("12") == 12


def test_rejects_text() -> None:
    """The promise of lesson 'Custom-exceptions' still holds."""
    with pytest.raises(ValueError):
        parse_age("old")
