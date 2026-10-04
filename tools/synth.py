"""Generate runnable lessons for topics nobody has hand written yet.

Three layers, tried in order:

1. :data:`RECIPES` - a keyword table holding real, tiny code.
2. A standard library module whose name matches the lesson slug.
3. A clearly marked draft that explains how to explore the topic.

Everything produced here is valid Python with passing tests.
:mod:`tools.verify` counts the drafts so later phases know what is left.
"""

from __future__ import annotations

import sys
from typing import Any, NamedTuple

from lesson_model import STATUS_DRAFT, Lesson, public_names

__all__ = ["synthesize", "recipe_count", "ok", "err"]


class Case(NamedTuple):
    """One generated test."""

    name: str
    statement: str
    error: str | None = None
    args: tuple[str, ...] = ()


def ok(name: str, statement: str, *args: str) -> Case:
    """Return a test case that must simply pass.

    Args:
        name: A short snake_case description.
        statement: The expression to assert.
        args: Extra pytest fixtures, such as ``tmp_path``.
    """
    return Case(name, statement, None, args)


def err(name: str, error: str, statement: str) -> Case:
    """Return a test case that must raise ``error``."""
    return Case(name, statement, error, ())


class Recipe(NamedTuple):
    """A tiny hand shaped lesson reused by every topic that matches."""

    keyword: str
    blurb: str
    points: tuple[str, ...]
    functions: str
    demo: str
    cases: tuple[Case, ...]
    practice: tuple[str, ...] = ()
    glossary: tuple[tuple[str, str], ...] = ()
    prelude: tuple[str, ...] = ()
    test_setup: str = ""


RECIPES: tuple[Recipe, ...] = (
    Recipe(
        keyword="hello",
        blurb="Every programmer starts by printing a friendly line.",
        points=("Call `print` to show text", "Put text between quotes", "Run a file with `python`"),
        functions='''
def greet(name: str) -> str:
    """Return a hello world line for one person.

    Args:
        name: Who to greet.

    Returns:
        A short greeting.

    Examples:
        >>> greet("Ada")
        'Hello, Ada!'
    """
    return f"Hello, {name}!"
''',
        demo='print(greet("world"))',
        cases=(ok("greets_by_name", 'greet("Ada") == "Hello, Ada!"'),),
        practice=("Change the name inside the quotes and run it again.",),
        glossary=(("print", "A built in function that shows a value on screen"),),
    ),
    Recipe(
        keyword="print",
        blurb="`print` shows values on the screen so you can see what your code did.",
        points=("`print` takes any value", "`sep` and `end` change the output", "`print` gives back `None`"),
        functions='''
def describe_person(name: str, age: int) -> str:
    """Return a short line about a person.

    Args:
        name: The person's name.
        age: The person's age in years.

    Returns:
        A line such as ``"Ada is 36 years old"``.
    """
    return f"{name} is {age} years old"


def banner(text: str, width: int = 3) -> str:
    """Return text wrapped in stars.

    Args:
        text: The text to wrap.
        width: The width of the banner.

    Returns:
        The wrapped text.

    Examples:
        >>> banner("hi")
        '*** hi ***'
        >>> banner("hi", 1)
        '* hi *'
    """
    return "*" * width + f" {text} " + "*" * width
''',
        demo='print(describe_person("Ada", 36))\nprint(banner("done"))',
        cases=(
            ok("describes", 'describe_person("Ada", 36) == "Ada is 36 years old"'),
            ok("wraps_text", 'banner("hi") == "*** hi ***"'),
        ),
    ),
    Recipe(
        keyword="input",
        blurb="`input` asks a question and waits for the answer.",
        points=("`input` always gives back text", "Wrap it in `int` to get a number", "Keep the prompt short"),
        functions='''
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
''',
        demo='print("Type something, then press enter.")',
        cases=(
            ok("cleans_an_answer", 'clean_answer("name", "name: Ada ") == "Ada"'),
            ok("keeps_empty", 'clean_answer("name", "   ") == ""'),
        ),
        glossary=(("stdin", "The stream of text that comes from the keyboard"),),
    ),
    Recipe(
        keyword="variable",
        blurb="A variable is a name that remembers a value.",
        points=("Create a variable with `=`", "One name can be given a new value", "Names use snake_case"),
        functions='''
def make_greeting(name: str) -> str:
    """Build a greeting for someone.

    Args:
        name: The person's name.

    Returns:
        A greeting that ends with an exclamation mark.

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
''',
        demo='print(make_greeting("Ada"))\nprint(swap(1, 2))',
        cases=(
            ok("greets", 'make_greeting("Ada") == "Hello, Ada!"'),
            ok("swaps", "swap(1, 2) == (2, 1)"),
            ok("swapping_twice_is_safe", "swap(*swap(1, 2)) == (1, 2)"),
        ),
        practice=("Add a third variable that holds your age and print all three.",),
        glossary=(
            ("variable", "A name that points at a value"),
            ("assignment", "Storing a value in a name with `=`"),
        ),
    ),
    Recipe(
        keyword="integer",
        blurb="Integers are whole numbers with no decimal part.",
        points=("`int` holds whole numbers", "Python integers never overflow", "`//` divides and drops the rest"),
        functions='''
def whole_pairs(count: int) -> int:
    """Return how many whole pairs a count makes.

    Args:
        count: How many things there are.

    Returns:
        The number of whole pairs.

    Examples:
        >>> whole_pairs(7)
        3
    """
    return count // 2


def is_even(number: int) -> bool:
    """Say whether a number divides by two with nothing left over.

    Args:
        number: The number to check.

    Returns:
        ``True`` when the number is even.

    Examples:
        >>> is_even(4)
        True
    """
    return number % 2 == 0
''',
        demo='print(whole_pairs(7))\nprint(is_even(4))',
        cases=(
            ok("counts_pairs", "whole_pairs(7) == 3"),
            ok("even_is_true", "is_even(4) is True"),
            ok("odd_is_false", "is_even(5) is False"),
        ),
        glossary=(("integer", "A whole number such as 0, 1 or -42"),),
    ),
    Recipe(
        keyword="float",
        blurb="Floats are numbers with a decimal point.",
        points=("`float` stores decimal numbers", "Adding floats can be a tiny bit off", "`round` tidies the result"),
        functions='''
def average(numbers: list[float]) -> float:
    """Return the mean of some numbers.

    Args:
        numbers: The numbers to average. Must not be empty.

    Returns:
        The mean, rounded to two decimal places.

    Raises:
        ValueError: If ``numbers`` is empty.

    Examples:
        >>> average([1.0, 2.0, 4.0])
        2.33
    """
    if not numbers:
        raise ValueError("need at least one number")
    return round(sum(numbers) / len(numbers), 2)
''',
        demo='print(average([1.0, 2.0, 4.0]))',
        cases=(
            ok("averages", "average([1.0, 2.0, 4.0]) == 2.33"),
            ok("single_number", "average([5.0]) == 5.0"),
            err("empty_list", "ValueError", "average([])"),
        ),
        practice=("Round the average to one decimal place instead of two.",),
        glossary=(("float", "A number with a decimal point, such as 1.5"),),
    ),
    Recipe(
        keyword="boolean",
        blurb="Booleans are just two values: `True` and `False`.",
        points=("Comparing makes a boolean", "`and`, `or` and `not` work on booleans", "`True` counts as 1"),
        functions='''
def is_odd(number: int) -> bool:
    """Say whether a number is odd.

    Args:
        number: The number to check.

    Returns:
        ``True`` when the number is odd.

    Examples:
        >>> is_odd(3)
        True
    """
    return number % 2 == 1


def both_yes(first: bool, second: bool) -> bool:
    """Say whether both answers are yes.

    Args:
        first: The first yes or no.
        second: The second yes or no.

    Returns:
        ``True`` only when both are ``True``.

    Examples:
        >>> both_yes(True, False)
        False
    """
    return first and second
''',
        demo='print(is_odd(3))\nprint(both_yes(True, False))',
        cases=(
            ok("three_is_odd", "is_odd(3) is True"),
            ok("two_is_not_odd", "is_odd(2) is False"),
            ok("and_needs_both", "both_yes(True, True) is True"),
        ),
        glossary=(("boolean", "A value that is only `True` or `False`"),),
    ),
    Recipe(
        keyword="string",
        blurb="Strings are text, and text is written between quotes.",
        points=("Join strings with `+`", "Use f-strings to place values inside text", "Strings cannot be changed"),
        functions='''
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


def count_words(sentence: str) -> int:
    """Count how many words are in a sentence.

    Args:
        sentence: The sentence to measure.

    Returns:
        The number of words.

    Examples:
        >>> count_words("a b c")
        3
    """
    return len(sentence.split())


def initials(name: str) -> str:
    """Return the initials of a full name.

    Args:
        name: A name such as ``"Ada Lovelace"``.

    Returns:
        The initials in upper case.

    Examples:
        >>> initials("Ada Lovelace")
        'AL'
    """
    return "".join(part[0] for part in name.split()).upper()
''',
        demo='print(shout("hello"))\nprint(count_words("one two three"))\nprint(initials("Ada Lovelace"))',
        cases=(
            ok("upper_cases", 'shout("hello") == "HELLO"'),
            ok("counts_words", 'count_words("a b c") == 3'),
            ok("makes_initials", 'initials("Ada Lovelace") == "AL"'),
        ),
        practice=("Write a function that counts the vowels in a word.",),
        glossary=(
            ("string", "Text made of characters"),
            ("immutable", "Cannot be changed after it is made"),
        ),
    ),
    Recipe(
        keyword="f-string",
        blurb="F-strings let you drop values straight into text.",
        points=("Write `f\"{value}\"` to insert a value", "Add `:.2f` to control the look", "No `str()` needed"),
        functions='''
def price_line(item: str, price: float) -> str:
    """Return one line of a receipt.

    Args:
        item: The name of the item.
        price: The price of one item.

    Returns:
        A line such as ``"Tea: 2.50"``.

    Examples:
        >>> price_line("Tea", 2.5)
        'Tea: 2.50'
    """
    return f"{item}: {price:.2f}"


def progress(done: int, total: int) -> str:
    """Return a tiny progress bar.

    Args:
        done: How many steps are finished.
        total: How many steps there are.

    Returns:
        A bar such as ``"[##----]"``.

    Examples:
        >>> progress(2, 6)
        '[##----]'
    """
    filled = round(done / total * 6)
    return "[" + "#" * filled + "-" * (6 - filled) + "]"
''',
        demo='print(price_line("Tea", 2.5))\nprint(progress(2, 6))',
        cases=(
            ok("formats_price", 'price_line("Tea", 2.5) == "Tea: 2.50"'),
            ok("draws_progress", 'progress(2, 6) == "[##----]"'),
        ),
        glossary=(("f-string", "A string with `{}` holes for values"),),
    ),
    Recipe(
        keyword="list",
        blurb="A list keeps many values in order.",
        points=("Make a list with `[ ]`", "Count items with `len`", "Add to the end with `append`"),
        functions='''
def add_up(numbers: list[int]) -> int:
    """Add every number in a list.

    Args:
        numbers: The numbers to add.

    Returns:
        The total.

    Examples:
        >>> add_up([1, 2, 3])
        6
    """
    return sum(numbers)


def biggest(numbers: list[int]) -> int:
    """Return the largest number in a list.

    Args:
        numbers: A list that is not empty.

    Returns:
        The largest number.

    Raises:
        ValueError: If the list is empty.

    Examples:
        >>> biggest([4, 9, 2])
        9
    """
    if not numbers:
        raise ValueError("list is empty")
    return max(numbers)
''',
        demo='print(add_up([1, 2, 3]))\nprint(biggest([4, 9, 2]))',
        cases=(
            ok("sums", "add_up([1, 2, 3]) == 6"),
            ok("finds_biggest", "biggest([4, 9, 2]) == 9"),
            err("empty_list", "ValueError", "biggest([])"),
        ),
        glossary=(("list", "An ordered box that can grow and shrink"),),
    ),
    Recipe(
        keyword="dictionary",
        blurb="A dictionary stores values under keys, like a phone book.",
        points=("Make a dictionary with `{ }`", "Look a value up by its key", "`get` gives a safe default"),
        functions='''
def word_lengths(text: str) -> dict[str, int]:
    """Map each word to the number of letters it has.

    Args:
        text: A sentence.

    Returns:
        A dictionary of word to length.

    Examples:
        >>> word_lengths("a bb")
        {'a': 1, 'bb': 2}
    """
    return {word: len(word) for word in text.split()}


def lookup(ages: dict[str, int], name: str) -> int:
    """Return someone's age, or ``-1`` when we do not know them.

    Args:
        ages: A mapping of name to age.
        name: The person to look up.

    Returns:
        The age, or ``-1``.

    Examples:
        >>> lookup({"Ada": 36}, "Bo")
        -1
    """
    return ages.get(name, -1)
''',
        demo='print(word_lengths("a bb ccc"))\nprint(lookup({"Ada": 36}, "Bo"))',
        cases=(
            ok("counts_words", 'word_lengths("a bb") == {"a": 1, "bb": 2}'),
            ok("missing_is_safe", 'lookup({}, "nobody") == -1'),
        ),
        glossary=(
            ("key", "The name you look up"),
            ("value", "The thing you find"),
        ),
    ),
    Recipe(
        keyword="tuple",
        blurb="A tuple is a list that cannot be changed.",
        points=("Make a tuple with `( )`", "Unpack it in one line", "Safe to use as a dictionary key"),
        functions='''
def first_and_last(numbers: tuple[int, ...]) -> tuple[int, int]:
    """Return the first and last number of a tuple.

    Args:
        numbers: A tuple with at least one number.

    Returns:
        The first and last number.

    Raises:
        ValueError: If the tuple is empty.

    Examples:
        >>> first_and_last((3, 4, 5))
        (3, 5)
    """
    if not numbers:
        raise ValueError("tuple is empty")
    return numbers[0], numbers[-1]


def swap(pair: tuple[int, int]) -> tuple[int, int]:
    """Swap the two numbers in a pair.

    Args:
        pair: Two numbers.

    Returns:
        The pair, backwards.

    Examples:
        >>> swap((1, 2))
        (2, 1)
    """
    left, right = pair
    return right, left
''',
        demo='print(first_and_last((3, 4, 5)))\nprint(swap((1, 2)))',
        cases=(
            ok("finds_ends", "first_and_last((3, 4, 5)) == (3, 5)"),
            ok("swaps", "swap((1, 2)) == (2, 1)"),
            err("empty_tuple", "ValueError", "first_and_last(())"),
        ),
        glossary=(("tuple", "A short, unchangeable sequence"),),
    ),
    Recipe(
        keyword="set",
        blurb="A set keeps unique values with no duplicates.",
        points=("Sets have no order", "Duplicates disappear", "`|` joins two sets"),
        functions='''
def unique_letters(text: str) -> set[str]:
    """Return every different letter in the text.

    Args:
        text: The text to look at.

    Returns:
        A set of letters.

    Examples:
        >>> sorted(unique_letters("aab"))
        ['a', 'b']
    """
    return set(text)


def shared(first: set[str], second: set[str]) -> set[str]:
    """Return the letters that appear in both sets.

    Args:
        first: The first set.
        second: The second set.

    Returns:
        The letters found in both.
    """
    return first & second
''',
        demo='print(sorted(unique_letters("banana")))\nprint(sorted(shared({"a", "b"}, {"b", "c"})))',
        cases=(
            ok("drops_repeats", 'unique_letters("aab") == {"a", "b"}'),
            ok("finds_common", 'shared({"a", "b"}, {"b"}) == {"b"}'),
        ),
        glossary=(("set", "A box of unique things with no order"),),
    ),
    Recipe(
        keyword="comprehension",
        blurb="A comprehension builds a new collection in one readable line.",
        points=("Start with the name you want", "`for` walks the items", "Add `if` to keep only some"),
        functions='''
def double_all(numbers: list[int]) -> list[int]:
    """Double every number.

    Args:
        numbers: The numbers to double.

    Returns:
        A new list of doubled numbers.

    Examples:
        >>> double_all([1, 2])
        [2, 4]
    """
    return [number * 2 for number in numbers]


def big_numbers(numbers: list[int]) -> list[int]:
    """Keep only the numbers bigger than ten.

    Args:
        numbers: The numbers to filter.

    Returns:
        The numbers that are bigger than ten.

    Examples:
        >>> big_numbers([5, 20])
        [20]
    """
    return [number for number in numbers if number > 10]
''',
        demo='print(double_all([1, 2, 3]))\nprint(big_numbers([5, 20, 30]))',
        cases=(
            ok("doubles", "double_all([1, 2]) == [2, 4]"),
            ok("filters", "big_numbers([5, 20]) == [20]"),
        ),
        glossary=(("comprehension", "A one line way to build a new list, set or dict"),),
    ),
    Recipe(
        keyword="slicing",
        blurb="Slicing takes a piece out of a sequence.",
        points=("`sequence[start:stop]`", "The end is not included", "Leave a side out to mean from that end"),
        functions='''
def first_three(items: list[int]) -> list[int]:
    """Return the first three items.

    Args:
        items: The list to cut.

    Returns:
        Up to three items from the front.

    Examples:
        >>> first_three([1, 2, 3, 4])
        [1, 2, 3]
    """
    return items[:3]


def middle(items: list[int]) -> list[int]:
    """Return everything except the first and last item.

    Args:
        items: The list to cut.

    Returns:
        The items in the middle.

    Examples:
        >>> middle([1, 2, 3])
        [2]
    """
    return items[1:-1]


def reversed_copy(items: list[int]) -> list[int]:
    """Return a new list that reads backwards.

    Args:
        items: The list to copy.

    Returns:
        A new, backwards list.
    """
    return items[::-1]
''',
        demo='print(first_three([1, 2, 3, 4]))\nprint(middle([1, 2, 3]))\nprint(reversed_copy([1, 2, 3]))',
        cases=(
            ok("takes_three", "first_three([1, 2, 3, 4]) == [1, 2, 3]"),
            ok("drops_ends", "middle([1, 2, 3]) == [2]"),
            ok("turns_around", "reversed_copy([1, 2, 3]) == [3, 2, 1]"),
        ),
        glossary=(
            ("slice", "The piece you cut out"),
            ("index", "The position of an item, starting at 0"),
        ),
    ),
    Recipe(
        keyword="function",
        blurb="A function is a named recipe you can run again and again.",
        points=("Define one with `def`", "Inputs are parameters", "`return` sends a value back"),
        functions='''
def area(width: float, height: float) -> float:
    """Return the area of a rectangle.

    Args:
        width: How wide it is.
        height: How tall it is.

    Returns:
        The area.

    Examples:
        >>> area(2.0, 3.0)
        6.0
    """
    return width * height


def describe(width: float, height: float) -> str:
    """Describe a rectangle in words.

    Args:
        width: How wide it is.
        height: How tall it is.

    Returns:
        A short sentence.
    """
    return f"A rectangle of {area(width, height)} square units."
''',
        demo='print(area(2.0, 3.0))\nprint(describe(2.0, 3.0))',
        cases=(
            ok("computes_area", "area(2.0, 3.0) == 6.0"),
            ok("describes", 'describe(2.0, 3.0) == "A rectangle of 6.0 square units."'),
        ),
        glossary=(
            ("function", "A named recipe that takes inputs and gives an answer"),
            ("return", "The value a function hands back"),
        ),
    ),
    Recipe(
        keyword="argument",
        blurb="Arguments are the values you hand to a function.",
        points=("Positional arguments go by position", "Keyword arguments go by name", "Defaults fill the blanks"),
        functions='''
def greet(name: str, greeting: str = "Hello") -> str:
    """Build a greeting.

    Args:
        name: Who to greet.
        greeting: The word to use first.

    Returns:
        The full greeting.

    Examples:
        >>> greet("Ada")
        'Hello, Ada'
        >>> greet("Ada", greeting="Hi")
        'Hi, Ada'
    """
    return f"{greeting}, {name}"


def total_price(cost: float, quantity: int, *, tax: float = 0.0) -> float:
    """Work out a price with tax.

    Args:
        cost: The price of one item.
        quantity: How many items.
        tax: The tax rate, so ``0.2`` means twenty percent.

    Returns:
        The full price, rounded to two decimals.
    """
    return round(cost * quantity * (1 + tax), 2)
''',
        demo='print(greet("Ada"))\nprint(total_price(2.5, 3, tax=0.2))',
        cases=(
            ok("default_greeting", 'greet("Ada") == "Hello, Ada"'),
            ok("keyword_greeting", 'greet("Ada", greeting="Hi") == "Hi, Ada"'),
            ok("adds_tax", "total_price(10.0, 2, tax=0.1) == 22.0"),
        ),
        glossary=(
            ("parameter", "The name in the function definition"),
            ("argument", "The value you pass in"),
        ),
    ),
    Recipe(
        keyword="return",
        blurb="`return` sends a value back to whoever called the function.",
        points=("`return` ends the function", "No `return` means `None`", "Return a tuple to return many values"),
        functions='''
def divide(pie: int, people: int) -> tuple[int, int]:
    """Share a pie as evenly as possible.

    Args:
        pie: How many pieces the pie has.
        people: How many people share it.

    Returns:
        Each person's share and the pieces left over.

    Raises:
        ValueError: If there are no people.

    Examples:
        >>> divide(8, 3)
        (2, 2)
    """
    if people == 0:
        raise ValueError("need at least one person")
    return divmod(pie, people)
''',
        demo='share, left = divide(8, 3)\nprint(f"each gets {share}, {left} left")',
        cases=(
            ok("splits_fairly", "divide(8, 3) == (2, 2)"),
            ok("no_left_over", "divide(9, 3) == (3, 0)"),
            err("no_people", "ValueError", "divide(8, 0)"),
        ),
        glossary=(("return", "Hand a value back to the caller"),),
    ),
    Recipe(
        keyword="lambda",
        blurb="A lambda is a tiny function with no name and no body.",
        points=("`lambda x: ...` makes a small function", "Perfect for sort keys", "Use `def` for anything longer"),
        functions='''
def add_tax(price: float) -> float:
    """Add twenty percent tax to a price.

    Args:
        price: The price before tax.

    Returns:
        The price with tax.

    Examples:
        >>> add_tax(10.0)
        12.0
    """
    with_tax = lambda value: round(value * 1.2, 2)
    return with_tax(price)


def by_length(words: list[str]) -> list[str]:
    """Sort words from longest to shortest.

    Args:
        words: The words to sort.

    Returns:
        A new sorted list.
    """
    return sorted(words, key=lambda word: len(word), reverse=True)
''',
        demo='print(add_tax(10.0))\nprint(by_length(["pear", "fig", "banana"]))',
        cases=(
            ok("adds_tax", "add_tax(10.0) == 12.0"),
            ok("sorts_long_first", 'by_length(["a", "ccc", "bb"]) == ["ccc", "bb", "a"]'),
        ),
        glossary=(("lambda", "A small nameless function"),),
    ),
    Recipe(
        keyword="closure",
        blurb="A closure is a function that remembers names from around it.",
        points=("Inner functions can read outer names", "`nonlocal` changes an outer name", "Great for counters"),
        functions='''
from collections.abc import Callable


def make_counter(start: int = 0) -> Callable[[], int]:
    """Make a counter that remembers how often it was called.

    Args:
        start: The number to start from.

    Returns:
        A function that counts 1, 2, 3 and so on from ``start``.

    Examples:
        >>> tick = make_counter()
        >>> tick(), tick()
        (1, 2)
    """
    count = start

    def tick() -> int:
        """Add one and return the new count."""
        nonlocal count
        count += 1
        return count

    return tick
''',
        demo='tick = make_counter()\nprint(tick(), tick(), tick())',
        cases=(
            ok("counts_from_one", "make_counter()() == 1"),
            ok("counts_from_a_start", "make_counter(10)() == 11"),
        ),
        glossary=(
            ("closure", "A function that remembers names from around it"),
            ("nonlocal", "Reach one scope out to change a name"),
        ),
    ),
    Recipe(
        keyword="recursion",
        blurb="Recursion is a function calling itself with a smaller problem.",
        points=("Every recursion needs a stopping point", "The base case comes first", "Recursion follows the shape of the data"),
        functions='''
def factorial(number: int) -> int:
    """Return the product of all numbers up to ``number``.

    Args:
        number: A whole number of 0 or more.

    Returns:
        The factorial.

    Examples:
        >>> factorial(5)
        120
    """
    if number <= 1:
        return 1
    return number * factorial(number - 1)


def total_length(text: str) -> int:
    """Return how many characters a string holds.

    Args:
        text: The string to measure.

    Returns:
        The number of characters.
    """
    if not text:
        return 0
    return len(text[0]) + total_length(text[1:])
''',
        demo='print(factorial(5))\nprint(total_length("hello"))',
        cases=(
            ok("factorial_of_five", "factorial(5) == 120"),
            ok("zero_is_one", "factorial(0) == 1"),
            ok("counts_characters", 'total_length("hello") == 5'),
        ),
        glossary=(
            ("recursion", "A function that calls itself"),
            ("base case", "The simple answer that stops the recursion"),
        ),
    ),
    Recipe(
        keyword="exception",
        blurb="Exceptions are how Python complains about problems.",
        points=("Errors stop the program", "`try` and `except` catch them", "`raise` sends one on purpose"),
        functions='''
def parse_age(text: str) -> int:
    """Turn text into an age.

    Args:
        text: The text to read.

    Returns:
        The age as a whole number.

    Raises:
        ValueError: If the text is not a whole number.

    Examples:
        >>> parse_age("12")
        12
    """
    try:
        return int(text)
    except ValueError as error:
        raise ValueError(f"age must be a whole number: {text!r}") from error
''',
        demo='print(parse_age("12"))\ntry:\n    print(parse_age("old"))\nexcept ValueError as error:\n    print(error)',
        cases=(
            ok("reads_a_number", 'parse_age("12") == 12'),
            err("rejects_text", "ValueError", 'parse_age("old")'),
        ),
        glossary=(
            ("exception", "A signal that something went wrong"),
            ("raise", "Send an exception on purpose"),
        ),
    ),
    Recipe(
        keyword="iterator",
        blurb="Iterators hand out one value at a time.",
        points=("`for` asks for values with `next`", "`iter` makes an iterator", "`StopIteration` ends it"),
        functions='''
def count_to(limit: int) -> int:
    """Count from one to a limit and return how many numbers there were.

    Args:
        limit: The last number to count.

    Returns:
        The amount of numbers counted.

    Examples:
        >>> count_to(3)
        3
    """
    how_many = 0
    for _ in range(limit):
        how_many += 1
    return how_many


def take_first(items: list[int], how_many: int) -> list[int]:
    """Take the first few items from a list using an iterator.

    Args:
        items: Where to take them from.
        how_many: How many to take.

    Returns:
        The items that were taken.
    """
    picker = iter(items)
    return [next(picker) for _ in range(how_many)]
''',
        demo='print(count_to(3))\nprint(take_first([9, 8, 7], 2))',
        cases=(
            ok("counts", "count_to(3) == 3"),
            ok("takes_two", "take_first([9, 8, 7], 2) == [9, 8]"),
        ),
        glossary=(("iterator", "A thing that gives values one by one"),),
    ),
    Recipe(
        keyword="generator",
        blurb="A generator makes values on demand and forgets them after.",
        points=("`yield` pauses a function", "Generators are lazy", "Loop over them like any list"),
        functions='''
def count_up(limit: int):
    """Yield the numbers from one to a limit.

    Args:
        limit: The last number to give.

    Yields:
        Each number in turn.

    Examples:
        >>> list(count_up(3))
        [1, 2, 3]
    """
    for number in range(1, limit + 1):
        yield number


def evens(limit: int):
    """Yield only the even numbers below a limit.

    Args:
        limit: The limit to stop at.

    Yields:
        Each even number in turn.
    """
    for number in range(0, limit, 2):
        yield number
''',
        demo='print(list(count_up(3)))\nprint(list(evens(7)))',
        cases=(
            ok("counts_up", "list(count_up(3)) == [1, 2, 3]"),
            ok("keeps_evens", "list(evens(7)) == [0, 2, 4, 6]"),
        ),
        glossary=(
            ("generator", "A function that gives values one at a time"),
            ("yield", "Pause and hand out one value"),
        ),
    ),
    Recipe(
        keyword="decorator",
        blurb="A decorator wraps a function to add behaviour.",
        points=("A decorator takes a function and gives a new one back", "`@` applies it", "`functools.wraps` keeps the name"),
        functions='''
from functools import wraps


def shouty(func):
    """Make a function's result louder.

    Args:
        func: The function to wrap.

    Returns:
        The wrapped function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Call the function and shout its result."""
        return str(func(*args, **kwargs)).upper()

    return wrapper


@shouty
def welcome(name: str) -> str:
    """Return a welcome message.

    Args:
        name: Who is arriving.

    Returns:
        A welcome message.
    """
    return f"welcome {name}"
''',
        demo='print(welcome("Ada"))\nprint(welcome.__name__)',
        cases=(
            ok("shouts_result", 'welcome("Ada") == "WELCOME ADA"'),
            ok("keeps_the_name", 'welcome.__name__ == "welcome"'),
        ),
        glossary=(
            ("decorator", "A function that wraps another function"),
            ("wrapper", "The new function a decorator gives back"),
        ),
    ),
    Recipe(
        keyword="class",
        blurb="A class is a blueprint for making objects.",
        points=("Classes group data and behaviour", "`self` is the object itself", "Call the class to make an object"),
        functions='''
class Dog:
    """A simple dog that can bark."""

    def __init__(self, name: str) -> None:
        """Give the dog a name.

        Args:
            name: The dog's name.
        """
        self.name = name

    def bark(self) -> str:
        """Return what the dog says.

        Returns:
            A bark that uses the dog's name.
        """
        return f"{self.name} says woof"
''',
        demo='dog = Dog("Rex")\nprint(dog.bark())',
        cases=(
            ok("barks", 'Dog("Rex").bark() == "Rex says woof"'),
            ok("keeps_the_name", 'Dog("Rex").name == "Rex"'),
        ),
        glossary=(
            ("class", "A blueprint for objects"),
            ("object", "One thing made from a class"),
            ("self", "The object a method is called on"),
        ),
    ),
    Recipe(
        keyword="file",
        blurb="Files let your code remember things after it stops.",
        points=("`open` a file to read or write", "`with` closes it for you", "Use `pathlib` for paths"),
        functions='''
from pathlib import Path


def save_lines(lines: list[str], path: str) -> int:
    """Write lines to a file and return how many were written.

    Args:
        lines: The lines to save.
        path: Where to save them.

    Returns:
        The number of lines written.
    """
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\\n".join(lines))
    return len(lines)


def read_lines(path: str) -> list[str]:
    """Read lines back from a file.

    Args:
        path: The file to read.

    Returns:
        The lines that were in the file.
    """
    return Path(path).read_text(encoding="utf-8").splitlines()
''',
        demo='import tempfile\n\nfolder = tempfile.mkdtemp()\ntarget = f"{folder}/demo.txt"\nprint(save_lines(["one", "two"], target))\nprint(read_lines(target))',
        cases=(
            ok(
                "round_trip",
                'save_lines(["one"], str(tmp_path / "demo.txt")) == 1 and read_lines(str(tmp_path / "demo.txt")) == ["one"]',
                "tmp_path",
            ),
        ),
        glossary=(
            ("file", "Text or data saved on disk"),
            ("context manager", "The object behind `with`, which tidies up for you"),
        ),
    ),
    Recipe(
        keyword="json",
        blurb="JSON is a plain text way to store lists and dictionaries.",
        points=("`json.loads` reads text", "`json.dumps` writes text", "Keys have to be text"),
        functions='''
import json


def to_json(data: dict) -> str:
    """Turn a dictionary into JSON text.

    Args:
        data: The data to store.

    Returns:
        The data as JSON.
    """
    return json.dumps(data, sort_keys=True)


def from_json(text: str) -> dict:
    """Read JSON text back into a dictionary.

    Args:
        text: The JSON text.

    Returns:
        The data inside.

    Raises:
        ValueError: If the text is not valid JSON.
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError as error:
        raise ValueError(f"not valid JSON: {text!r}") from error
''',
        demo='text = to_json({"name": "Ada", "age": 36})\nprint(text)\nprint(from_json(text))',
        cases=(
            ok("writes_json", 'to_json({"a": 1}) == \'{"a": 1}\''),
            ok("reads_json", 'from_json(\'{"a": 1}\') == {"a": 1}'),
            err("bad_json", "ValueError", "from_json('nope')"),
        ),
        glossary=(("JSON", "A plain text format for lists and dictionaries"),),
    ),
    Recipe(
        keyword="test",
        blurb="Tests are code that checks your code still works.",
        points=("Write one test per behaviour", "Use `assert` to check", "Run them with `pytest`"),
        functions='''
def add(first: int, second: int) -> int:
    """Add two numbers.

    Args:
        first: The first number.
        second: The second number.

    Returns:
        The total.
    """
    return first + second
''',
        demo='print(add(2, 3))',
        cases=(
            ok("adds_small_numbers", "add(2, 3) == 5"),
            ok("adds_zero", "add(0, 0) == 0"),
        ),
        glossary=(
            ("test", "A check that a piece of code behaves"),
            ("assert", "A line that must be true or the test fails"),
        ),
    ),
    Recipe(
        keyword="async",
        blurb="`async` lets one program wait for many slow things at once.",
        points=("`async def` makes a coroutine", "`await` waits without blocking", "`asyncio.gather` runs them together"),
        functions='''
import asyncio


async def double(number: int) -> int:
    """Double a number after a tiny pause.

    Args:
        number: The number to double.

    Returns:
        The doubled number.
    """
    await asyncio.sleep(0)
    return number * 2


async def double_all(numbers: list[int]) -> list[int]:
    """Double many numbers at the same time.

    Args:
        numbers: The numbers to double.

    Returns:
        The doubled numbers, in order.
    """
    return list(await asyncio.gather(*(double(number) for number in numbers)))
''',
        demo='import asyncio\n\nprint(asyncio.run(double_all([1, 2, 3])))',
        cases=(
            ok("doubles_all", "asyncio.run(double_all([1, 2])) == [2, 4]"),
        ),
        test_setup="import asyncio\n",
        glossary=(
            ("coroutine", "A function that waits using `await`"),
            ("event loop", "The scheduler that runs waiting code"),
        ),
    ),
    Recipe(
        keyword="thread",
        blurb="Threads run many tasks at once inside one program.",
        points=("A thread is a helper of the program", "Share data carefully", "Use a lock when sharing"),
        functions='''
from concurrent.futures import ThreadPoolExecutor


def double(number: int) -> int:
    """Double a number.

    Args:
        number: The number to double.

    Returns:
        The doubled number.
    """
    return number * 2


def double_all(numbers: list[int]) -> list[int]:
    """Double many numbers using a pool of threads.

    Args:
        numbers: The numbers to double.

    Returns:
        The doubled numbers, in order.
    """
    with ThreadPoolExecutor(max_workers=4) as pool:
        return list(pool.map(double, numbers))
''',
        demo='print(double_all([1, 2, 3]))',
        cases=(ok("doubles_with_threads", "double_all([1, 2, 3]) == [2, 4, 6]"),),
        glossary=(("thread", "A helper that runs at the same time as the program"),),
    ),
    Recipe(
        keyword="type-hint",
        blurb="Type hints describe what a function expects and gives back.",
        points=("Write `: int` after a parameter", "`-> str` after the parameters", "Hints help readers and checkers"),
        functions='''
def double(number: int) -> int:
    """Double a number.

    Args:
        number: The number to double.

    Returns:
        The doubled number.
    """
    return number * 2


def average(numbers: list[float]) -> float:
    """Return the mean of some numbers.

    Args:
        numbers: A non empty list of numbers.

    Returns:
        The mean.
    """
    return sum(numbers) / len(numbers)
''',
        demo='print(double(4))\nprint(average([1.0, 2.0]))',
        cases=(
            ok("doubles", "double(4) == 8"),
            ok("averages", "average([1.0, 3.0]) == 2.0"),
        ),
        glossary=(("type hint", "A note about the type of a value"),),
    ),
    Recipe(
        keyword="dataclass",
        blurb="A dataclass writes the boring parts of a class for you.",
        points=("`@dataclass` builds `__init__` for you", "Every field needs a type", "`frozen=True` stops changes"),
        functions='''
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    """A point on a grid."""

    x: int
    y: int

    def distance_from_origin(self) -> float:
        """Return how far the point is from ``0, 0``.

        Returns:
            The distance, as a float.
        """
        return (self.x**2 + self.y**2) ** 0.5
''',
        demo='point = Point(3, 4)\nprint(point)\nprint(round(point.distance_from_origin(), 2))',
        cases=(
            ok("keeps_values", "Point(3, 4).x == 3"),
            ok("measures_distance", "Point(3, 4).distance_from_origin() == 5.0"),
            err("cannot_change", "Exception", "setattr(Point(1, 1), 'x', 2)"),
        ),
        glossary=(("dataclass", "A class that generates its own `__init__`"),),
    ),
    Recipe(
        keyword="context-manager",
        blurb="`with` sets something up and always tidies it away.",
        points=("`with` opens and closes for you", "Safe even when the body raises", "Files, locks and sockets all use it"),
        functions='''
from contextlib import contextmanager


@contextmanager
def announce(title: str):
    """Print a title before and after a block of code.

    Args:
        title: The title to print.

    Yields:
        The block to run.
    """
    print(f"start: {title}")
    yield
    print(f"end: {title}")
''',
        demo='with announce("demo"):\n    print("working")',
        cases=(
            ok("has_enter", 'hasattr(announce("x"), "__enter__")'),
            ok("has_exit", 'hasattr(announce("x"), "__exit__")'),
        ),
        glossary=(("context manager", "An object that sets up and tidies up"),),
    ),
    Recipe(
        keyword="argparse",
        blurb="`argparse` reads command line arguments for you.",
        points=("Describe each argument", "Read them from `sys.argv`", "`--help` comes free"),
        functions='''
import argparse


def build_parser() -> argparse.ArgumentParser:
    """Make the argument reader for a tiny tool.

    Returns:
        A parser that understands ``name`` and ``--times``.
    """
    parser = argparse.ArgumentParser(description="Say hello a few times.")
    parser.add_argument("name", help="who to greet")
    parser.add_argument("--times", type=int, default=1, help="how many greetings")
    return parser


def greeting_for(name: str, times: int) -> str:
    """Build the greeting lines.

    Args:
        name: Who to greet.
        times: How many lines to make.

    Returns:
        The lines joined by newlines.
    """
    return "\\n".join(f"Hello, {name}!" for _ in range(times))
''',
        demo='print(greeting_for("Ada", 2))',
        cases=(
            ok("greets_twice", 'greeting_for("Ada", 2) == "Hello, Ada!\\nHello, Ada!"'),
            ok("greets_once", 'greeting_for("Ada", 1) == "Hello, Ada!"'),
        ),
        glossary=(("argument", "A value typed on the command line"),),
    ),
    Recipe(
        keyword="logging",
        blurb="Logging writes notes about what your program is doing.",
        points=("Use levels such as info and error", "Log to the screen or to a file", "Libraries should not use `print`"),
        functions='''
import logging

logger = logging.getLogger("lesson")


def make_logger(level: int = logging.INFO) -> logging.Logger:
    """Return a logger that writes short messages.

    Args:
        level: The lowest level to show.

    Returns:
        The configured logger.
    """
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")
    return logger


def log_a_journey(steps: list[str]) -> list[str]:
    """Log each step and return the steps.

    Args:
        steps: The steps to log.

    Returns:
        The same steps, unchanged.
    """
    for step in steps:
        logger.info("step: %s", step)
    return steps
''',
        demo='make_logger()\nprint(log_a_journey(["start", "stop"]))',
        cases=(ok("keeps_steps", 'log_a_journey(["a", "b"]) == ["a", "b"]'),),
        glossary=(("logging", "Recorded notes about how a program behaves"),),
    ),
    Recipe(
        keyword="sqlite",
        blurb="SQLite keeps your data in one file and understands real SQL.",
        points=("`sqlite3.connect` opens a database file", "Use `?` to keep SQL safe", "`with` commits or rolls back"),
        functions='''
import sqlite3


def create_table(db: sqlite3.Connection) -> None:
    """Make the notes table if it is not there yet.

    Args:
        db: An open connection.
    """
    with db:
        db.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT)")


def add_note(db: sqlite3.Connection, text: str) -> int:
    """Save one note and return its row id.

    Args:
        db: An open connection.
        text: The note to save.

    Returns:
        The new note's id.
    """
    with db:
        cursor = db.execute("INSERT INTO notes (text) VALUES (?)", (text,))
        return int(cursor.lastrowid or 0)


def all_notes(db: sqlite3.Connection) -> list[str]:
    """Return every saved note, oldest first.

    Args:
        db: An open connection.

    Returns:
        The note texts.
    """
    rows = db.execute("SELECT text FROM notes ORDER BY id").fetchall()
    return [row[0] for row in rows]
''',
        demo='import sqlite3\n\ndb = sqlite3.connect(":memory:")\ncreate_table(db)\nadd_note(db, "milk")\nprint(all_notes(db))',
        cases=(
            ok("saves_and_reads", 'notes_round_trip() == ["milk"]'),
        ),
        test_setup='''
def notes_round_trip() -> list[str]:
    """Save one note in a memory database and read it back.

    Returns:
        The notes that were found.
    """
    db = sqlite3.connect(":memory:")
    create_table(db)
    add_note(db, "milk")
    return all_notes(db)
''',
        prelude=("import sqlite3",),
        glossary=(
            ("SQL", "The language databases understand"),
            ("transaction", "A group of changes that all succeed or all fail"),
        ),
    ),
    Recipe(
        keyword="regex",
        blurb="Regular expressions find patterns inside text.",
        points=("`re.search` finds the first match", "Raw strings keep backslashes readable", "Groups capture pieces"),
        functions='''
import re


def find_digits(text: str) -> list[str]:
    """Return every run of digits in the text.

    Args:
        text: The text to search.

    Returns:
        The digit groups, in order.

    Examples:
        >>> find_digits("a1 b22")
        ['1', '22']
    """
    return re.findall(r"\\d+", text)


def is_valid_pin(pin: str) -> bool:
    """Say whether a pin is exactly four digits.

    Args:
        pin: The pin to check.

    Returns:
        ``True`` when the pin is four digits.

    Examples:
        >>> is_valid_pin("1234")
        True
    """
    return bool(re.fullmatch(r"\\d{4}", pin))
''',
        demo='print(find_digits("a1 b22"))\nprint(is_valid_pin("1234"), is_valid_pin("12"))',
        cases=(
            ok("finds_digits", 'find_digits("a1 b22") == ["1", "22"]'),
            ok("checks_pin", 'is_valid_pin("1234") is True'),
        ),
        glossary=(("regex", "A small language for finding text patterns"),),
    ),
    Recipe(
        keyword="benchmark",
        blurb="Timing code shows which way is faster.",
        points=("`timeit` runs code many times", "Compare two versions", "Never trust a single run"),
        functions='''
import timeit


def slow_total(numbers: list[int]) -> int:
    """Add numbers one at a time.

    Args:
        numbers: The numbers to add.

    Returns:
        The total.
    """
    total = 0
    for number in numbers:
        total += number
    return total


def measure(function, numbers: list[int], rounds: int = 3) -> float:
    """Return how many seconds one call takes.

    Args:
        function: The function to time.
        numbers: What to give it.
        rounds: How many times to try.

    Returns:
        The fastest run in seconds.
    """
    timer = timeit.Timer(lambda: function(numbers))
    return min(timer.repeat(repeat=rounds, number=1))
''',
        demo='print(f"{measure(slow_total, list(range(100))):.6f} seconds")',
        cases=(
            ok("adds_correctly", "slow_total([1, 2, 3]) == 6"),
            ok("measures_time", "measure(slow_total, [1, 2]) >= 0.0"),
        ),
        glossary=(("benchmark", "A careful measurement of how long code takes"),),
    ),
)

GENERIC_POINTS = (
    "Find the official documentation and skim it",
    "Try the smallest possible example in the REPL",
    "Write the one sentence that explains the idea in your own words",
)


def _source(title: str, blurb: str, functions: str, demo: str, folder: str, module: str) -> str:
    header = [
        f'"""{title}.',
        "",
        blurb,
        "",
        "Run me:",
        f"    python {folder}/{module}.py",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "",
    ]
    body = [line.rstrip() for line in functions.strip("\n").splitlines()]
    footer = [
        "",
        "",
        "def main() -> None:",
        '    """Print a small demo so the lesson is runnable."""',
        *(f"    {line}" if line.strip() else "" for line in demo.strip("\n").splitlines()),
        "",
        "",
        'if __name__ == "__main__":',
        "    main()",
        "",
    ]
    return "\n".join(header + body + footer)


def _tests(
    title: str,
    module: str,
    source: str,
    cases: tuple[Case, ...],
    prelude: tuple[str, ...] = (),
    setup: str = "",
) -> str:
    names = ", ".join(public_names(source))
    needs_pytest = any(case.error for case in cases)
    lines = [f'"""Tests for {title}."""', ""]
    for line in prelude:
        lines.append(line)
    if prelude:
        lines.append("")
    if names:
        lines.append(f"from {module} import {names}")
    else:
        lines.append(f"import {module}")
    if needs_pytest:
        lines += ["", "import pytest"]
    lines += ["", ""]
    if setup:
        lines += [setup.rstrip(), "", ""]
    if not cases or not names:
        lines += [
            "def test_imports() -> None:",
            '    """The example module can be imported."""',
            f"    assert {module}",
            "",
        ]
        return "\n".join(lines)
    for case in cases:
        parameters = ", ".join(case.args)
        lines.append(f"def test_{case.name}({parameters}) -> None:")
        lines.append(f'    """The promise of lesson {title!r} still holds."""')
        if case.error:
            lines += [f"    with pytest.raises({case.error}):", f"        {case.statement}"]
        else:
            lines.append(f"    assert {case.statement}")
        lines += ["", ""]
    return "\n".join(lines).rstrip() + "\n"


def _lesson(
    topic: Any,
    blurb: str,
    points: tuple[str, ...],
    functions: str,
    demo: str,
    cases: tuple[Case, ...],
    practice: tuple[str, ...] = (),
    glossary: tuple[tuple[str, str], ...] = (),
    prelude: tuple[str, ...] = (),
    setup: str = "",
) -> Lesson:
    source = _source(topic.title, blurb, functions, demo, topic.folder, topic.module)
    return Lesson(
        blurb=blurb,
        points=points,
        source=source,
        tests=_tests(topic.title, topic.module, source, cases, prelude, setup),
        practice=practice,
        glossary=glossary,
        status=STATUS_DRAFT,
    )


def _recipe_lesson(topic: Any, recipe: Recipe) -> Lesson:
    return _lesson(
        topic,
        recipe.blurb,
        recipe.points,
        recipe.functions,
        recipe.demo,
        recipe.cases,
        recipe.practice,
        recipe.glossary,
        recipe.prelude,
        recipe.test_setup,
    )


def _stdlib_lesson(topic: Any) -> Lesson | None:
    name = topic.slug.replace("-", "_")
    if not name.isidentifier() or name not in sys.stdlib_module_names:
        return None
    blurb = f"`{name}` is a standard library module. This lesson shows how to look inside one."
    functions = f'''
def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import {name}

    return getattr({name}, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names {name} offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import {name}

    return sorted(item for item in dir({name}) if not item.startswith("_"))
'''
    return _lesson(
        topic,
        blurb,
        (f"Import `{name}` and see what it holds", "Use `dir` to list what a module offers", "Read the module's own docs"),
        functions,
        "print(module_path())\nprint(len(public_names()), 'public names')",
        (
            ok("has_a_path", "isinstance(module_path(), str)"),
            ok("lists_names", "isinstance(public_names(), list)"),
        ),
        (f"Open the REPL, `import {name}`, then call `dir({name})`.",),
        ((name, f"A standard library module for {topic.slug.replace('-', ' ')}"),),
    )


def _explore_lesson(topic: Any) -> Lesson:
    blurb = f"Placeholder for **{topic.title}**. A later phase replaces this with a full lesson."
    functions = f'''
def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({{"{topic.slug.replace("-", " ")}"}})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\\n".join(f"{{step}}. {topic.title}" for step in (1, 2, 3))
'''
    return _lesson(
        topic,
        blurb,
        GENERIC_POINTS,
        functions,
        "print(outline())\nprint(keywords())",
        (
            ok("has_keywords", "len(keywords()) == 1"),
            ok("has_three_steps", 'len(outline().splitlines()) == 3'),
        ),
        (
            "Replace this lesson with a real one: add two small functions with docstrings.",
            "Add one test per function.",
        ),
    )


def _singular_forms(phrase: str) -> set[str]:
    """Return a phrase plus simple singular spellings, for recipe matching."""
    forms = {phrase}
    if phrase.endswith("ies") and len(phrase) > 3:
        forms.add(phrase[:-3] + "y")
    if phrase.endswith("es") and len(phrase) > 2:
        forms.add(phrase[:-2])
    if phrase.endswith("s") and len(phrase) > 1:
        forms.add(phrase[:-1])
    return forms


def synthesize(topic: Any) -> Lesson:
    """Return a generated lesson for a topic nobody has hand written.

    Args:
        topic: A :class:`tools.curriculum.Topic`.

    Returns:
        A ready to render lesson, marked as a draft.
    """
    words = topic.slug.replace("_", "-").split("-")
    for length in (3, 2, 1):
        for start in range(len(words) - length + 1):
            phrase = "-".join(words[start : start + length])
            for form in _singular_forms(phrase):
                for recipe in RECIPES:
                    if recipe.keyword == form:
                        return _recipe_lesson(topic, recipe)
    return _stdlib_lesson(topic) or _explore_lesson(topic)


def recipe_count() -> int:
    """Return how many keyword recipes exist."""
    return len(RECIPES)
