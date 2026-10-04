"""Tests for Python-bytecode."""

from lesson_862_python_bytecode import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Python-bytecode' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Python-bytecode' still holds."""
    assert len(outline().splitlines()) == 3
