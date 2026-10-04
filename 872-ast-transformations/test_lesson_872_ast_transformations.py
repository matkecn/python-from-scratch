"""Tests for Ast-transformations."""

from lesson_872_ast_transformations import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Ast-transformations' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Ast-transformations' still holds."""
    assert len(outline().splitlines()) == 3
