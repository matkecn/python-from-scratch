"""Input-validation.

`input` asks a question and waits for the answer.

Run me:
    python 678-input-validation/lesson_678_input_validation.py
"""

from __future__ import annotations


def clean_answer(question: str, answer: str) -> str:
    """Tidy an answer that was typed by a human.

    Args:
        question: The question that was asked.
        answer: What the person typed.

    Returns:
        The answer, trimmed and with the question removed.

    Examples:
        >>> clean_answer("name", "name: Ada ")
        'Ada'
    """
    return answer.replace(question, "", 1).strip(" :")


def ask(question: str) -> str:
    """Ask a question and clean up the answer.

    Args:
        question: The question to ask.

    Returns:
        The answer without extra spaces.
    """
    return clean_answer(question, input(f"{question} "))


def ask_number(question: str) -> int:
    """Ask for a whole number and keep asking until we get one.

    Args:
        question: The question to ask.

    Returns:
        The number the user typed.
    """
    while True:
        try:
            return int(ask(question))
        except ValueError:
            print("Please type a whole number.")


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print("Type something, then press enter.")


if __name__ == "__main__":
    main()
