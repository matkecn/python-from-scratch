"""Hand written lessons 011 to 020: printing, asking, and your first program."""

from __future__ import annotations

from lesson_model import Lesson

__all__ = ["LESSONS"]


def lesson(
    blurb: str,
    points: tuple[str, ...],
    source: str,
    tests: str,
    practice: tuple[str, ...] = (),
    glossary: tuple[tuple[str, str], ...] = (),
    read_more: tuple[str, ...] = (),
) -> Lesson:
    """Return a hand written lesson.

    Args:
        blurb: One friendly sentence.
        points: Bullets for the "You will learn" section.
        source: The whole example module.
        tests: The whole test module.
        practice: Notebook and README exercises.
        glossary: Words to remember.
        read_more: Extra documentation links.

    Returns:
        A lesson ready to render.
    """
    return Lesson(
        blurb=blurb,
        points=points,
        source=source,
        tests=tests,
        practice=practice,
        glossary=glossary,
        read_more=read_more,
    )


LESSONS: dict[int, Lesson] = {
    11: lesson(
        blurb="`print` shows a value. `return` hands it back. They are not the same.",
        points=(
            "`print` writes to the screen for people",
            "`return` gives a value back to code",
            "Change the gap with `sep` and the ending with `end`",
        ),
        glossary=(
            ("side effect", "Something a program does that a caller cannot see, like printing"),
            ("return", "Handing a value back to whoever called"),
        ),
        source='''"""Print.

`print` is for people. `return` is for code. A function that returns a value
can be printed later, reused and tested.

Run me:
    python 011-print/lesson_011_print.py
"""

from __future__ import annotations


def shout(text: str) -> str:
    """Return the text in upper case.

    Args:
        text: The text to shout.

    Returns:
        The same text, louder.

    Examples:
        >>> shout("hello")
        'HELLO'
    """
    return text.upper()


def show(text: str, times: int = 1) -> None:
    """Print some text a number of times.

    Args:
        text: The text to print.
        times: How many lines to print.
    """
    for _ in range(times):
        print(text)


def join_numbers(numbers: list[int]) -> str:
    """Return numbers as one line, separated by dashes.

    Args:
        numbers: The numbers to join.

    Returns:
        A single line of text.

    Examples:
        >>> join_numbers([1, 2, 3])
        '1 - 2 - 3'
    """
    return " - ".join(str(number) for number in numbers)


def main() -> None:
    """Show printing and returning side by side."""
    print(shout("hello"))
    show("again", times=2)
    print(join_numbers([1, 2, 3]))


if __name__ == "__main__":
    main()
''',
        tests='''"""Tests for Print."""

from lesson_011_print import join_numbers, shout, show


def test_shout_returns_text() -> None:
    """The value comes back, it is not printed."""
    assert shout("hello") == "HELLO"


def test_show_prints_nothing_useful(capsys) -> None:
    """`show` prints and gives back None."""
    show("hi", times=2)
    assert capsys.readouterr().out == "hi\\nhi\\n"


def test_join_numbers() -> None:
    """Numbers can be joined into a line of text."""
    assert join_numbers([1, 2, 3]) == "1 - 2 - 3"
''',
        practice=(
            "Print the same value twice, once with `print` and once with `return`.",
            "Use `sep` and `end` to print `1, 2, 3` on one line without trailing spaces.",
        ),
    ),
    12: lesson(
        blurb="Ask a question with `input`, then check what came back.",
        points=(
            "`input` always returns text",
            "Turn text into a number with `int`",
            "Keep asking until the answer makes sense",
        ),
        glossary=(
            ("prompt", "The question shown before waiting for an answer"),
            ("validation", "Checking an answer is usable"),
        ),
        source='''"""Input.

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
''',
        tests='''"""Tests for Input."""

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
''',
        practice=(
            "Ask for a name and an age, then print a birthday message.",
            "Make `ask_number` also accept a float, such as `7.5`.",
        ),
    ),
    13: lesson(
        blurb="A variable is a name that remembers a value.",
        points=(
            "Store a value with `=`",
            "Change a name as often as you like",
            "Swap two values in one line",
        ),
        glossary=(
            ("variable", "A name that points at a value"),
            ("assignment", "Storing a value in a name"),
        ),
        source='''"""Variables.

A variable is a label you stick on a value. `=` does not mean equals, it means
"put this value in this box".

Run me:
    python 013-variables/lesson_013_variables.py
"""

from __future__ import annotations


def make_greeting(name: str) -> str:
    """Build a greeting for someone.

    Args:
        name: The person's name.

    Returns:
        A greeting ending with an exclamation mark.

    Examples:
        >>> make_greeting("Ada")
        'Hello, Ada!'
    """
    return f"Hello, {name}!"


def swap(first: int, second: int) -> tuple[int, int]:
    """Return two numbers in the opposite order.

    Args:
        first: The number that should end up second.
        second: The number that should end up first.

    Returns:
        The two numbers, swapped.

    Examples:
        >>> swap(1, 2)
        (2, 1)
    """
    return second, first


def describe_box(box: int) -> str:
    """Describe a variable in words.

    Args:
        box: The value inside the box.

    Returns:
        A sentence about the value and its type.

    Examples:
        >>> describe_box(3)
        'the box holds 3, which is type int'
    """
    return f"the box holds {box}, which is type {type(box).__name__}"


def main() -> None:
    """Make a few variables and look at them."""
    name = "Ada"
    year = 1815
    print(make_greeting(name))
    print(describe_box(year))
    left, right = swap(1, 2)
    print(f"swapped: left={left}, right={right}")


if __name__ == "__main__":
    main()
''',
        tests='''"""Tests for Variables."""

from lesson_013_variables import describe_box, make_greeting, swap


def test_greeting_uses_the_name() -> None:
    """A name in, a greeting out."""
    assert make_greeting("Ada") == "Hello, Ada!"


def test_swap_turns_them_around() -> None:
    """The first value comes back second."""
    assert swap(1, 2) == (2, 1)


def test_swapping_twice_is_safe() -> None:
    """Two swaps leave the pair as it started."""
    assert swap(*swap(1, 2)) == (1, 2)


def test_describe_box_names_the_type() -> None:
    """We can see the value and its type in one sentence."""
    assert describe_box(3) == "the box holds 3, which is type int"
''',
        practice=(
            "Make three variables for a character and print a one line story about them.",
            "Swap three values using one line and no temporary variable.",
        ),
    ),
    14: lesson(
        blurb="Good names make code readable without comments.",
        points=(
            "Use `snake_case` for names",
            "Use UPPER CASE for constants",
            "Avoid names that hide built ins",
        ),
        glossary=(
            ("snake_case", "Words joined with underscores, like `total_price`"),
            ("constant", "A name that should never change, written in UPPER CASE"),
        ),
        source='''"""Naming.

Names are the cheapest documentation in programming. `total_price` tells you
more than `tp`.

Run me:
    python 014-naming/lesson_014_naming.py
"""

from __future__ import annotations

import keyword

TAX_RATE = 0.2


def to_snake_case(text: str) -> str:
    """Turn words into a snake_case name.

    Args:
        text: Words separated by spaces, dashes or capitals.

    Returns:
        A name using only lowercase letters, digits and underscores.

    Examples:
        >>> to_snake_case("Total Price")
        'total_price'
        >>> to_snake_case("total-price")
        'total_price'
    """
    cleaned = "".join(character.lower() if character.isalnum() else "_" for character in text)
    while "__" in cleaned:
        cleaned = cleaned.replace("__", "_")
    return cleaned.strip("_")


def is_valid_name(name: str) -> bool:
    """Say whether a name is safe to use.

    Args:
        name: The name to check.

    Returns:
        ``True`` when the name starts with a letter, holds only letters,
        digits and underscores, and is not a Python keyword.

    Examples:
        >>> is_valid_name("total_price")
        True
        >>> is_valid_name("2fast")
        False
        >>> is_valid_name("class")
        False
    """
    if not name.isidentifier() or keyword.iskeyword(name):
        return False
    return not name.startswith("_")


def hides_a_builtin(name: str) -> bool:
    """Say whether a name would hide something Python already has.

    Args:
        name: The name to check.

    Returns:
        ``True`` for names such as ``list`` or ``id``.

    Examples:
        >>> hides_a_builtin("list")
        True
        >>> hides_a_builtin("total_price")
        False
    """
    import builtins

    return hasattr(builtins, name)


def total_price(cost: float, quantity: int) -> float:
    """Return a price with tax added.

    Args:
        cost: The price of one item.
        quantity: How many items.

    Returns:
        The full price, rounded to two decimals.
    """
    return round(cost * quantity * (1 + TAX_RATE), 2)


def main() -> None:
    """Look at some names."""
    print(to_snake_case("Total Price"))
    print(f"total_price is a fine name: {is_valid_name('total_price')}")
    print(f"'list' hides a builtin: {hides_a_builtin('list')}")
    print(total_price(10.0, 2))


if __name__ == "__main__":
    main()
''',
        tests='''"""Tests for Naming."""

from lesson_014_naming import hides_a_builtin, is_valid_name, to_snake_case, total_price


def test_snake_case_from_words() -> None:
    """Spaces become underscores."""
    assert to_snake_case("Total Price") == "total_price"


def test_snake_case_from_dashes() -> None:
    """Dashes become underscores too."""
    assert to_snake_case("total-price") == "total_price"


def test_valid_names() -> None:
    """Lowercase words joined by underscores are fine."""
    assert is_valid_name("total_price") is True


def test_bad_names() -> None:
    """Names cannot start with a digit or be a keyword."""
    assert is_valid_name("2fast") is False
    assert is_valid_name("class") is False


def test_private_names_are_rejected() -> None:
    """A leading underscore is a private convention, not a normal name."""
    assert is_valid_name("_hidden") is False


def test_spots_hidden_builtins() -> None:
    """Using `list` as a variable would hide the real one."""
    assert hides_a_builtin("list") is True
    assert hides_a_builtin("total_price") is False


def test_price_includes_tax() -> None:
    """Two items at ten each plus twenty percent tax."""
    assert total_price(10.0, 2) == 24.0
''',
        practice=(
            "Rename three variables in a file you wrote so the names explain themselves.",
            "Write `bad_names(names)` that returns the names you should not use.",
        ),
    ),
    15: lesson(
        blurb="`=` assigns, `==` compares. Learning the difference saves hours.",
        points=(
            "`=` puts a value in a name",
            "`==` asks whether two values match",
            "`+=` and friends update in place",
        ),
        glossary=(
            ("assignment", "Putting a value into a name"),
            ("augmented assignment", "An update such as `total += 1`"),
        ),
        source='''"""Assignment.

``=`` copies a value into a name. ``==`` asks a question. Mixing them up is the
most common small bug in Python.

Run me:
    python 015-assignment/lesson_015_assignment.py
"""

from __future__ import annotations


def are_equal(first: int, second: int) -> bool:
    """Say whether two numbers match.

    Args:
        first: The number on the left.
        second: The number on the right.

    Returns:
        ``True`` when they are equal.

    Examples:
        >>> are_equal(2, 2)
        True
        >>> are_equal(2, 3)
        False
    """
    return first == second


def add_to_total(total: int, amount: int = 1) -> int:
    """Add to a running total.

    Args:
        total: The total so far.
        amount: How much to add.

    Returns:
        The new total.
    """
    total += amount
    return total


def chain() -> tuple[int, int, int]:
    """Show that one value can wear three names.

    Returns:
        Three copies of the same number.

    Examples:
        >>> chain()
        (7, 7, 7)
    """
    first = second = third = 7
    return first, second, third


def count_down(start: int) -> list[int]:
    """Return the numbers from start down to one.

    Args:
        start: The number to start from.

    Returns:
        The numbers, largest first.

    Examples:
        >>> count_down(3)
        [3, 2, 1]
    """
    numbers = list(range(start, 0, -1))
    return numbers


def main() -> None:
    """Compare, then update."""
    total = 0
    for amount in [5, 3, 2]:
        total = add_to_total(total, amount)
    print(f"total is {total}, equal to 10? {are_equal(total, 10)}")
    print(count_down(3))


if __name__ == "__main__":
    main()
''',
        tests='''"""Tests for Assignment."""

from lesson_015_assignment import add_to_total, are_equal, chain, count_down


def test_equal_numbers() -> None:
    """Two equals means a question, not an assignment."""
    assert are_equal(2, 2) is True
    assert are_equal(2, 3) is False


def test_adding_to_a_total() -> None:
    """The new total comes back."""
    assert add_to_total(4) == 5
    assert add_to_total(4, 6) == 10


def test_chaining_gives_one_value_three_names() -> None:
    """All three names hold the same number."""
    assert chain() == (7, 7, 7)


def test_counts_down() -> None:
    """The list runs from start to one."""
    assert count_down(3) == [3, 2, 1]
''',
        practice=(
            "Write a line that uses `=` and the same line with `==`, then predict each result.",
            "Add a `halve` function that divides a total in place.",
        ),
    ),
    16: lesson(
        blurb="An expression has a value. A statement just does something.",
        points=(
            "Expressions produce values such as `2 + 3`",
            "Statements do work such as `print(x)`",
            "Every statement is an expression, but not the other way round",
        ),
        glossary=(
            ("expression", "Code that produces a value"),
            ("statement", "A complete instruction"),
        ),
        source='''"""Expressions.

An expression is any piece of code that gives back a value. A statement is a
complete instruction. `2 + 3` is an expression. `print(2 + 3)` is a statement
that uses one.

Run me:
    python 016-expressions/lesson_016_expressions.py
"""

from __future__ import annotations

OPERATORS = ("+", "-", "*", "/", "//", "%", "**")


def describe(value: object) -> str:
    """Return a value together with its type.

    Args:
        value: Anything at all.

    Returns:
        Text such as ``"5 (int)"``.

    Examples:
        >>> describe(5)
        '5 (int)'
    """
    return f"{value!r} ({type(value).__name__})"


def evaluate(expression: str) -> object:
    """Work out the value of a simple arithmetic expression.

    Only use this with expressions you trust.

    Args:
        expression: Something like ``"2 + 3"``.

    Returns:
        The value the expression produces.

    Raises:
        SyntaxError: If the text is not an expression.

    Examples:
        >>> evaluate("2 + 3")
        5
        >>> evaluate("2 ** 8")
        256
    """
    return eval(expression, {"__builtins__": {}}, {})  # noqa: S307


def is_expression(line: str) -> bool:
    """Say whether a line of text is an expression.

    Args:
        line: One line of code.

    Returns:
        ``True`` when the line produces a value on its own.

    Examples:
        >>> is_expression("2 + 3")
        True
        >>> is_expression("total = 2 + 3")
        False
    """
    try:
        tree = compile(line, "<lesson>", "eval")
    except SyntaxError:
        return False
    return bool(tree)


def main() -> None:
    """Compare an expression with a statement."""
    print(describe(evaluate("2 + 3")))
    print(f"'2 + 3' is an expression: {is_expression('2 + 3')}")
    print(f"'total = 2 + 3' is an expression: {is_expression('total = 2 + 3')}")


if __name__ == "__main__":
    main()
''',
        tests='''"""Tests for Expressions."""

import pytest

from lesson_016_expressions import describe, evaluate, is_expression


def test_describe_value_and_type() -> None:
    """We show the value and the type."""
    assert describe(5) == "5 (int)"


def test_evaluate_arithmetic() -> None:
    """Expressions produce values."""
    assert evaluate("2 + 3") == 5
    assert evaluate("2 ** 8") == 256


def test_evaluate_refuses_words() -> None:
    """A name is not defined in our tiny sandbox."""
    with pytest.raises(NameError):
        evaluate("some_name")


def test_recognises_expressions() -> None:
    """A bare calculation is an expression."""
    assert is_expression("2 + 3") is True


def test_assignment_is_not_an_expression() -> None:
    """Putting a value in a name is a statement."""
    assert is_expression("total = 2 + 3") is False
''',
        practice=(
            "Find three lines in your code that are expressions and three that are not.",
            "Use `is_expression` on a file you wrote and see what it says.",
        ),
    ),
    17: lesson(
        blurb="One instruction per line. Python reads top to bottom.",
        points=(
            "A statement is a complete instruction",
            "Lines run from the top down",
            "Indentation changes what a line belongs to",
        ),
        glossary=(
            ("statement", "One complete instruction"),
            ("program flow", "The order instructions run in"),
        ),
        source='''"""Statements.

Python reads your file from the top down, one statement at a time. It does not
skip ahead and it does not run ahead.

Run me:
    python 017-statements/lesson_017_statements.py
"""

from __future__ import annotations

CLOSERS = {"}", "]", ")"}


def count_statements(lines: list[str]) -> int:
    """Count the lines that actually do something.

    Args:
        lines: The lines of a Python file.

    Returns:
        The number of real statements.

    Examples:
        >>> count_statements(["x = 1", "", "# note", "print(x)"])
        2
    """
    total = 0
    for line in lines:
        text = line.strip()
        if not text or text.startswith("#"):
            continue
        if text in CLOSERS:
            continue
        total += 1
    return total


def first_three_statements(lines: list[str]) -> list[str]:
    """Return the first three real statements, trimmed.

    Args:
        lines: The lines of a Python file.

    Returns:
        Up to three statements.

    Examples:
        >>> first_three_statements(["a = 1", "b = 2", "c = 3", "d = 4"])
        ['a = 1', 'b = 2', 'c = 3']
    """
    statements = [
        line.strip()
        for line in lines
        if line.strip() and not line.strip().startswith("#") and line.strip() not in CLOSERS
    ]
    return statements[:3]


def runs_in_order(lines: list[str]) -> list[str]:
    """Return the statements in the order Python would run them.

    Args:
        lines: The lines of a Python file.

    Returns:
        The statements, top down.

    Examples:
        >>> runs_in_order(["b = 2", "a = 1"])
        ['b = 2', 'a = 1']
    """
    return first_three_statements(lines)


def main() -> None:
    """Count and show the statements in a tiny program."""
    program = [
        "# count to three",
        "for number in range(1, 4):",
        "    print(number)",
        "",
        "print('done')",
    ]
    print(f"{count_statements(program)} statements")
    for statement in runs_in_order(program):
        print(f"  {statement}")


if __name__ == "__main__":
    main()
''',
        tests='''"""Tests for Statements."""

from lesson_017_statements import count_statements, first_three_statements, runs_in_order


def test_counts_real_statements() -> None:
    """Blank lines and comments do not count."""
    assert count_statements(["x = 1", "", "# note", "print(x)"]) == 2


def test_takes_the_first_three() -> None:
    """We never take more than three."""
    assert first_three_statements(["a = 1", "b = 2", "c = 3", "d = 4"]) == ["a = 1", "b = 2", "c = 3"]


def test_handles_short_files() -> None:
    """Fewer than three statements is fine."""
    assert first_three_statements(["a = 1"]) == ["a = 1"]


def test_keeps_the_file_order() -> None:
    """Python does not sort your code for you."""
    assert runs_in_order(["b = 2", "a = 1"]) == ["b = 2", "a = 1"]
''',
        practice=(
            "Count the statements in a file you wrote.",
            "Predict the output of a five line program, then run it to check.",
        ),
    ),
    18: lesson(
        blurb="Keywords are the words Python keeps for itself.",
        points=(
            "There are only a few dozen keywords",
            "`keyword.iskeyword` checks a word",
            "You cannot use a keyword as a name",
        ),
        glossary=(
            ("keyword", "A word Python reserves for its own use"),
            ("soft keyword", "A word that is only special in certain places, such as `match`"),
        ),
        source='''"""Keywords.

Keywords are the words Python owns. You cannot use them as names, which is a
small price for a language that reads the same everywhere.

Run me:
    python 018-keywords/lesson_018_keywords.py
"""

from __future__ import annotations

import keyword

EXAMPLES = {
    "if": "starts a condition",
    "for": "starts a loop",
    "def": "starts a function",
    "return": "sends a value back",
    "class": "starts a class",
    "True": "a value that is always on",
}


def is_keyword(word: str) -> bool:
    """Say whether a word belongs to Python.

    Args:
        word: The word to check.

    Returns:
        ``True`` when Python reserves it.

    Examples:
        >>> is_keyword("if")
        True
        >>> is_keyword("iffy")
        False
    """
    return keyword.iskeyword(word)


def explain(word: str) -> str:
    """Say what a keyword is for.

    Args:
        word: The keyword to explain.

    Returns:
        A short sentence, or a note that the word is not a keyword.

    Examples:
        >>> explain("for")
        'for starts a loop'
        >>> explain("banana")
        "'banana' is not a Python keyword"
    """
    if word in EXAMPLES:
        return f"{word} {EXAMPLES[word]}"
    if is_keyword(word):
        return f"{word} is a Python keyword"
    return f"{word!r} is not a Python keyword"


def all_keywords() -> list[str]:
    """Return every keyword Python has.

    Returns:
        A sorted list of keywords.
    """
    return sorted(keyword.kwlist)


def safe_name(word: str) -> str:
    """Return a usable version of a word.

    Args:
        word: The word you would like to use.

    Returns:
        The word with a trailing underscore when Python owns it.

    Examples:
        >>> safe_name("class")
        'class_'
        >>> safe_name("total")
        'total'
    """
    return f"{word}_" if is_keyword(word) else word


def main() -> None:
    """Look at a few keywords."""
    for word in ("if", "for", "def", "banana"):
        print(explain(word))
    print(f"{len(all_keywords())} keywords in total")


if __name__ == "__main__":
    main()
''',
        tests='''"""Tests for Keywords."""

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
''',
        practice=(
            "Print all the keywords and find the three longest.",
            "Write a function that renames every keyword in a list of variable names.",
        ),
    ),
    19: lesson(
        blurb="Built in functions come with Python. You do not have to write them.",
        points=(
            "`len`, `sum`, `min` and `max` are always there",
            "`dir` shows what an object can do",
            "`help` explains anything",
        ),
        glossary=(
            ("built in", "Something Python gives you without importing"),
            ("namespace", "The names Python knows at the moment"),
        ),
        source='''"""Builtins.

Open Python and type `print`. It was already there. Everything in this lesson
was also already there, waiting for you.

Run me:
    python 019-builtins/lesson_019_builtins.py
"""

from __future__ import annotations

import builtins

HANDY = ("len", "sum", "min", "max", "sorted", "round", "abs", "print")


def builtin_names() -> list[str]:
    """Return every built in name Python offers.

    Returns:
        A sorted list of names.
    """
    return sorted(name for name in dir(builtins) if not name.startswith("_"))


def exists(name: str) -> bool:
    """Say whether Python has a built in with this name.

    Args:
        name: The name to look for.

    Returns:
        ``True`` when Python has it.

    Examples:
        >>> exists("len")
        True
        >>> exists("banana")
        False
    """
    return hasattr(builtins, name)


def use_these() -> str:
    """Use several built in functions and describe the results.

    Returns:
        A short report.

    Examples:
        >>> "3" in use_these()
        True
    """
    numbers = [4, 1, 3]
    return (
        f"len is {len(numbers)}, sum is {sum(numbers)}, "
        f"min is {min(numbers)}, max is {max(numbers)}, sorted is {sorted(numbers)}"
    )


def abilities(value: object) -> list[str]:
    """Return what an object can do.

    Args:
        value: Anything, such as a list.

    Returns:
        The public names the object has.

    Examples:
        >>> "append" in abilities([])
        True
    """
    return sorted(name for name in dir(value) if not name.startswith("_"))


def main() -> None:
    """Show what comes free with Python."""
    print(f"{len(builtin_names())} built in names")
    print(use_these())
    print(f"a list can: {', '.join(abilities([])[:5])} ...")


if __name__ == "__main__":
    main()
''',
        tests='''"""Tests for Builtins."""

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
''',
        practice=(
            "Find three built in functions you did not know and use them today.",
            "Use `help` on `sorted` and read the first line it prints.",
        ),
    ),
    20: lesson(
        blurb="Put everything together: a tiny quiz program that really runs.",
        points=(
            "Keep questions and answers in one list",
            "Score answers and give feedback",
            "Split a program into small functions",
        ),
        glossary=(
            ("quiz", "A small program that asks questions and checks answers"),
            ("score", "How many answers were right"),
        ),
        source='''"""First program.

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
''',
        tests='''"""Tests for First program."""

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
''',
        practice=(
            "Add two more questions of your own.",
            "Make the quiz ask again when the answer is wrong.",
        ),
    ),
}
