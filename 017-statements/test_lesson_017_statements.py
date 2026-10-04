"""Tests for Statements."""

from lesson_017_statements import count_statements, first_three_statements, runs_in_order


def test_counts_real_statements() -> None:
    """Blank lines and comments do not count."""
    assert count_statements(["x = 1", "", "# note", "print(x)"]) == 2


def test_takes_the_first_three() -> None:
    """We never take more than three."""
    assert first_three_statements(["a = 1", "b = 2", "c = 3", "d = 4"]) == ["a = 1", "b = 2", "c = 3"]


def test_handles_short_files() -> None:
    """Fewer than three statements is fine."""
    assert first_three_statements(["a = 1"]) == ["a = 1"]


def test_keeps_the_file_order() -> None:
    """Python does not sort your code for you."""
    assert runs_in_order(["b = 2", "a = 1"]) == ["b = 2", "a = 1"]
