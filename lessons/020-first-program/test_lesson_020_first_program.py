"""Tests for First program."""

from lesson_020_first_program import QUESTIONS, is_correct, play, report


def test_quiz_has_questions() -> None:
    """Every question comes with its answer."""
    assert len(QUESTIONS) >= 3
    for question, answer in QUESTIONS:
        assert question.endswith("?")
        assert answer


def test_correct_answers() -> None:
    """Case and spaces do not matter."""
    assert is_correct("4", "4") is True
    assert is_correct(" Blue ", "blue") is True


def test_wrong_answers() -> None:
    """A different answer is simply wrong."""
    assert is_correct("5", "4") is False


def test_playing_with_monkeypatch(monkeypatch) -> None:
    """Answer everything correctly and the score is full marks."""
    answers = iter([answer for _question, answer in QUESTIONS])
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(answers))
    assert play() == (len(QUESTIONS), len(QUESTIONS))


def test_playing_with_wrong_answers(monkeypatch) -> None:
    """Wrong answers give a score of zero."""
    wrong = iter(["nope" for _question, _answer in QUESTIONS])
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(wrong))
    assert play() == (0, len(QUESTIONS))


def test_reports_a_perfect_score() -> None:
    """Full marks get their own message."""
    assert report(3, 3) == "You got 3 out of 3 right. Perfect!"


def test_reports_a_good_score() -> None:
    """More than half is nearly there."""
    assert report(2, 3) == "You got 2 out of 3 right. Nearly there!"


def test_reports_a_low_score() -> None:
    """Less than half asks for practice."""
    assert "Keep practising" in report(0, 3)


def test_reports_an_empty_quiz() -> None:
    """No questions is handled kindly."""
    assert "no questions" in report(0, 0)
