"""Tests for Print."""

from lesson_011_print import join_numbers, shout, show


def test_shout_returns_text() -> None:
    """The value comes back, it is not printed."""
    assert shout("hello") == "HELLO"


def test_show_prints_nothing_useful(capsys) -> None:
    """`show` prints and gives back None."""
    show("hi", times=2)
    assert capsys.readouterr().out == "hi\nhi\n"


def test_join_numbers() -> None:
    """Numbers can be joined into a line of text."""
    assert join_numbers([1, 2, 3]) == "1 - 2 - 3"
