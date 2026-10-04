"""Tests for Builtins."""

from lesson_019_builtins import abilities, builtin_names, exists, use_these


def test_finds_builtins() -> None:
    """len comes with Python."""
    assert exists("len") is True
    assert exists("banana") is False


def test_builtin_list_is_sorted_and_unique() -> None:
    """The list is tidy."""
    names = builtin_names()
    assert names == sorted(set(names))
    assert "print" in names


def test_uses_several_builtins() -> None:
    """len, sum, min and max all work together."""
    report = use_these()
    assert "len is 3" in report
    assert "sum is 8" in report


def test_lists_what_an_object_can_do() -> None:
    """dir shows us the tools of an object."""
    names = abilities([])
    assert "append" in names
    assert not any(name.startswith("_") for name in names)
