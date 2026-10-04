"""Tests for Comments."""

from lesson_009_comments import count_comments, is_comment, strip_comment, why_not_what


def test_finds_comment_lines() -> None:
    """A line that starts with # is a comment."""
    assert is_comment("# a note") is True
    assert is_comment("   # indented note") is True


def test_code_with_a_note_is_not_a_comment_line() -> None:
    """Code followed by a note is still code."""
    assert is_comment("total = 1  # a note") is False


def test_strips_the_note() -> None:
    """What is left is the code."""
    assert strip_comment("total = 1  # add one") == "total = 1"


def test_a_whole_comment_becomes_nothing() -> None:
    """Stripping a comment line leaves an empty string."""
    assert strip_comment("# only a note") == ""


def test_counts_comments() -> None:
    """Only pure comment lines are counted."""
    assert count_comments(["# one", "x = 1", "# two"]) == 2


def test_the_rule_mentions_why() -> None:
    """Good comments explain why."""
    assert "why" in why_not_what()
