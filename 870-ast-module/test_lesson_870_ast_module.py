"""Tests for Ast-module."""

from lesson_870_ast_module import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Ast-module' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Ast-module' still holds."""
    assert len(outline().splitlines()) == 3
