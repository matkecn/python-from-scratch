"""Tests for Ast-generation."""

from lesson_873_ast_generation import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Ast-generation' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Ast-generation' still holds."""
    assert len(outline().splitlines()) == 3
