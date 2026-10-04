"""Tests for Json-load."""

from lesson_482_json_load import to_json, from_json

import pytest


def test_writes_json() -> None:
    """The promise of lesson 'Json-load' still holds."""
    assert to_json({"a": 1}) == '{"a": 1}'


def test_reads_json() -> None:
    """The promise of lesson 'Json-load' still holds."""
    assert from_json('{"a": 1}') == {"a": 1}


def test_bad_json() -> None:
    """The promise of lesson 'Json-load' still holds."""
    with pytest.raises(ValueError):
        from_json('nope')
