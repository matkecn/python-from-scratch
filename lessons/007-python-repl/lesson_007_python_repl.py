"""Python REPL.

Type ``python3`` and Python waits for you. That waiting prompt is the REPL.

Run me:
    python 007-python-repl/lesson_007_python_repl.py
"""

from __future__ import annotations

PARTS = ("read", "evaluate", "print", "loop")


def evaluate(expression: str) -> object:
    """Work out the value of a small expression.

    Only use this with code you trust. It runs the text as Python.

    Args:
        expression: The expression, such as ``"2 ** 10"``.

    Returns:
        Whatever the expression produced.

    Examples:
        >>> evaluate("2 ** 10")
        1024
        >>> evaluate("'py' + 'thon'")
        'python'
    """
    return eval(expression, {"__builtins__": {}}, {})  # noqa: S307


def describe(expression: str) -> str:
    """Return an expression's value together with its type.

    Args:
        expression: The expression to look at.

    Returns:
        Text such as ``"1024 (int)"``.

    Examples:
        >>> describe("2 + 2")
        '4 (int)'
    """
    value = evaluate(expression)
    return f"{value!r} ({type(value).__name__})"


def explain() -> str:
    """Return one line explaining what the REPL stands for.

    Returns:
        The four steps, in order.

    Examples:
        >>> explain()
        'read, evaluate, print, loop'
    """
    return ", ".join(PARTS)


def main() -> None:
    """Try a few expressions."""
    print(explain())
    for expression in ("2 + 2", "2 ** 10", "'py' + 'thon'", "[1, 2, 3]"):
        print(f"{expression:>14}  ->  {describe(expression)}")


if __name__ == "__main__":
    main()
