"""Tests for Json-custom-types."""

from lesson_485_json_custom_types import to_json, from_json

import pytest


def test_writes_json() -> None:
    """The promise of lesson 'Json-custom-types' still holds."""
    assert to_json({"a": 1}) == '{"a": 1}'


def test_reads_json() -> None:
    """The promise of lesson 'Json-custom-types' still holds."""
    assert from_json('{"a": 1}') == {"a": 1}


def test_bad_json() -> None:
    """The promise of lesson 'Json-custom-types' still holds."""
    with pytest.raises(ValueError):
        from_json('nope')
