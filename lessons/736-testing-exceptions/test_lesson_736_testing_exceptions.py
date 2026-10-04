"""Tests for Testing-exceptions."""

from lesson_736_testing_exceptions import parse_age

import pytest


def test_reads_a_number() -> None:
    """The promise of lesson 'Testing-exceptions' still holds."""
    assert parse_age("12") == 12


def test_rejects_text() -> None:
    """The promise of lesson 'Testing-exceptions' still holds."""
    with pytest.raises(ValueError):
        parse_age("old")
