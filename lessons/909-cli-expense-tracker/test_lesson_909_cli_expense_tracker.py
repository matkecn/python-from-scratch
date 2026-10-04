"""Tests for Cli-expense-tracker."""

from lesson_909_cli_expense_tracker import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Cli-expense-tracker' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Cli-expense-tracker' still holds."""
    assert len(outline().splitlines()) == 3
