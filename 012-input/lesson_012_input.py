"""Input.

`input` pauses and waits. Whatever you type comes back as text, even numbers.

Run me:
    python 012-input/lesson_012_input.py
"""

from __future__ import annotations


def clean(question: str, answer: str) -> str:
    """Tidy an answer a human typed.

    Args:
        question: The question that was asked.
        answer: What the person typed.

    Returns:
        The answer without the question and without extra spaces.

    Examples:
        >>> clean("Your name", "Your name: Ada ")
        'Ada'
        >>> clean("Your name", "  ")
        ''
    """
    return answer.replace(question, "", 1).strip(" :")


def ask(question: str) -> str:
    """Ask a question and return the tidy answer.

    Args:
        question: The question to ask.

    Returns:
        What the person typed, cleaned up.
    """
    return clean(question, input(f"{question}: "))


def ask_number(question: str) -> int:
    """Ask for a whole number and keep asking until we get one.

    Args:
        question: The question to ask.

    Returns:
        The number the person typed.

    Raises:
        ValueError: Never. Bad answers simply mean asking again.
    """
    while True:
        answer = clean(question, input(f"{question}: "))
        try:
            return int(answer)
        except ValueError:
            print("Please type a whole number, such as 7.")


def ask_yes_no(question: str) -> bool:
    """Ask a yes or no question.

    Args:
        question: The question to ask.

    Returns:
        ``True`` for yes, ``False`` for no.
    """
    answer = clean(question, input(f"{question} (y/n): ")).lower()
    return answer.startswith("y")


def main() -> None:
    """Ask a question, then say what we heard."""
    try:
        name = ask("Your name")
    except EOFError:
        print("Nobody typed anything, so we stop here.")
        return
    print(f"Hello, {name or 'stranger'}!")


if __name__ == "__main__":
    main()
