"""Tests for Json-serialization."""

from lesson_484_json_serialization import to_json, from_json

import pytest


def test_writes_json() -> None:
    """The promise of lesson 'Json-serialization' still holds."""
    assert to_json({"a": 1}) == '{"a": 1}'


def test_reads_json() -> None:
    """The promise of lesson 'Json-serialization' still holds."""
    assert from_json('{"a": 1}') == {"a": 1}


def test_bad_json() -> None:
    """The promise of lesson 'Json-serialization' still holds."""
    with pytest.raises(ValueError):
        from_json('nope')
