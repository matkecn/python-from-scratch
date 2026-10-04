"""Tests for Keywords."""

from lesson_018_keywords import all_keywords, explain, is_keyword, safe_name


def test_knows_keywords() -> None:
    """Python owns words like if and for."""
    assert is_keyword("if") is True
    assert is_keyword("iffy") is False


def test_explains_a_keyword() -> None:
    """We say what it is for."""
    assert explain("for") == "for starts a loop"


def test_explains_a_normal_word() -> None:
    """A normal word gets a clear answer."""
    assert "not a Python keyword" in explain("banana")


def test_lists_keywords() -> None:
    """The list is not empty and has no duplicates."""
    words = all_keywords()
    assert "if" in words
    assert len(words) == len(set(words))


def test_renames_a_unsafe_name() -> None:
    """A trailing underscore makes a keyword usable."""
    assert safe_name("class") == "class_"
    assert safe_name("total") == "total"
