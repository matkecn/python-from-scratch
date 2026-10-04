"""Tests for Cpython-vs-pypy."""

from lesson_883_cpython_vs_pypy import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Cpython-vs-pypy' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Cpython-vs-pypy' still holds."""
    assert len(outline().splitlines()) == 3
