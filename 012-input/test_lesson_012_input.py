"""Tests for Input."""

from lesson_012_input import ask_yes_no, ask_number, clean


def test_clean_removes_the_question() -> None:
    """The question is not part of the answer."""
    assert clean("Your name", "Your name: Ada ") == "Ada"


def test_clean_handles_empty_answers() -> None:
    """Nothing typed is nothing returned."""
    assert clean("Your name", "   ") == ""


def test_ask_number_rejects_words(monkeypatch) -> None:
    """We ask again when the answer is not a number."""
    answers = iter(["seven", "7"])
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(answers))
    assert ask_number("Age") == 7


def test_ask_yes_no(monkeypatch) -> None:
    """A y means yes."""
    monkeypatch.setattr("builtins.input", lambda _prompt="": "y")
    assert ask_yes_no("Ready") is True


def test_ask_no(monkeypatch) -> None:
    """Anything else means no."""
    monkeypatch.setattr("builtins.input", lambda _prompt="": "nope")
    assert ask_yes_no("Ready") is False
