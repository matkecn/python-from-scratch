"""Tests for Python-protocol-project."""

from lesson_450_python_protocol_project import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Python-protocol-project' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Python-protocol-project' still holds."""
    assert len(outline().splitlines()) == 3
