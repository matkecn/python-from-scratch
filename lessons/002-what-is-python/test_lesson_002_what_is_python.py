"""Tests for What is Python."""

from lesson_002_what_is_python import implementation, python_version, runs_bytecode, summary


def test_implementation_is_text() -> None:
    """The implementation comes back as text."""
    assert isinstance(implementation(), str)
    assert implementation()


def test_version_has_three_parts() -> None:
    """The version reads like 3.12.0."""
    assert python_version().count(".") == 2


def test_bytecode_matches_the_implementation() -> None:
    """Only CPython, in this course, runs bytecode."""
    assert runs_bytecode() == (implementation() == "CPython")


def test_summary_mentions_python() -> None:
    """The summary always says the word Python."""
    assert "CPython" in summary() or "Python" in summary()
