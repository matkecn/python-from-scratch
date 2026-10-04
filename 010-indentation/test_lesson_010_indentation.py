"""Tests for Indentation."""

from lesson_010_indentation import block_depth, count_statements, indent_width, opens_a_block


def test_measures_indentation() -> None:
    """We count the spaces at the start of a line."""
    assert indent_width("    print(1)") == 4
    assert indent_width("print(1)") == 0


def test_finds_block_openers() -> None:
    """A line ending in a colon starts a block."""
    assert opens_a_block("if ready:") is True
    assert opens_a_block("    print(1)") is False


def test_finds_the_deepest_block() -> None:
    """Nested blocks go deeper."""
    assert block_depth(["if a:", "    print(1)", "    for b in c:", "        print(2)"]) == 8


def test_empty_code_has_no_depth() -> None:
    """Nothing means nothing."""
    assert block_depth([]) == 0


def test_counts_only_real_statements() -> None:
    """Blank lines and comments are not statements."""
    assert count_statements(["x = 1", "", "# note", "print(x)"]) == 2
