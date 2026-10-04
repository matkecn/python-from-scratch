"""Tests for Assignment."""

from lesson_015_assignment import add_to_total, are_equal, chain, count_down


def test_equal_numbers() -> None:
    """Two equals means a question, not an assignment."""
    assert are_equal(2, 2) is True
    assert are_equal(2, 3) is False


def test_adding_to_a_total() -> None:
    """The new total comes back."""
    assert add_to_total(4) == 5
    assert add_to_total(4, 6) == 10


def test_chaining_gives_one_value_three_names() -> None:
    """All three names hold the same number."""
    assert chain() == (7, 7, 7)


def test_counts_down() -> None:
    """The list runs from start to one."""
    assert count_down(3) == [3, 2, 1]
