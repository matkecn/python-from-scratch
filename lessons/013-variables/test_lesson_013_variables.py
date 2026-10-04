"""Tests for Variables."""

from lesson_013_variables import describe_box, make_greeting, swap


def test_greeting_uses_the_name() -> None:
    """A name in, a greeting out."""
    assert make_greeting("Ada") == "Hello, Ada!"


def test_swap_turns_them_around() -> None:
    """The first value comes back second."""
    assert swap(1, 2) == (2, 1)


def test_swapping_twice_is_safe() -> None:
    """Two swaps leave the pair as it started."""
    assert swap(*swap(1, 2)) == (1, 2)


def test_describe_box_names_the_type() -> None:
    """We can see the value and its type in one sentence."""
    assert describe_box(3) == "the box holds 3, which is type int"
