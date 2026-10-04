"""Tests for Ast-parsing."""

from lesson_871_ast_parsing import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Ast-parsing' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Ast-parsing' still holds."""
    assert len(outline().splitlines()) == 3
