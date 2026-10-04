"""First program.

Everything so far, in one small program: a list of questions, a loop, a
condition, a score, and a friendly message at the end.

Run me:
    python 020-first-program/lesson_020_first_program.py
"""

from __future__ import annotations

QUESTIONS: tuple[tuple[str, str], ...] = (
    ("What is 2 + 2?", "4"),
    ("What colour is the sky on a clear day?", "blue"),
    ("How many legs does a spider have?", "8"),
)


def is_correct(given: str, expected: str) -> bool:
    """Say whether an answer is right.

    Args:
        given: What the player typed.
        expected: The answer we wanted.

    Returns:
        ``True`` when they match, ignoring case and extra spaces.

    Examples:
        >>> is_correct(" Blue ", "blue")
        True
    """
    return given.strip().lower() == expected.strip().lower()


def ask(question: str) -> str:
    """Ask one question.

    Args:
        question: The question to ask.

    Returns:
        The player's answer, cleaned up.
    """
    return input(f"{question} ").strip()


def play(questions: tuple[tuple[str, str], ...] = QUESTIONS) -> tuple[int, int]:
    """Ask every question and count the right answers.

    Args:
        questions: Pairs of question and answer.

    Returns:
        How many were right and how many were asked.
    """
    score = 0
    for question, expected in questions:
        if is_correct(ask(question), expected):
            score += 1
            print("  correct!")
        else:
            print(f"  the answer was {expected}")
    return score, len(questions)


def report(score: int, total: int) -> str:
    """Return a friendly summary of the score.

    Args:
        score: How many were right.
        total: How many were asked.

    Returns:
        A sentence to print at the end.

    Examples:
        >>> report(2, 3)
        'You got 2 out of 3 right. Nearly there!'
    """
    if total == 0:
        return "There were no questions. Come back later."
    if score == total:
        return f"You got {score} out of {total} right. Perfect!"
    if score * 2 >= total:
        return f"You got {score} out of {total} right. Nearly there!"
    return f"You got {score} out of {total} right. Keep practising!"


def main() -> None:
    """Run the quiz."""
    print("Welcome to the quiz!")
    try:
        score, total = play()
    except EOFError:
        print("Nobody typed anything, so the quiz stops here.")
        return
    print(report(score, total))


if __name__ == "__main__":
    main()
