"""Tests for Installation."""

from lesson_003_installation import check, find_python, is_installed


def test_python_can_be_found() -> None:
    """There is always a Python to run these tests."""
    assert find_python()


def test_installed_agrees_with_find_python() -> None:
    """We do not contradict ourselves."""
    assert is_installed() == bool(find_python())


def test_check_mentions_the_path() -> None:
    """The report shows where Python lives."""
    assert find_python() in check()
