# 016 · Expressions

An expression has a value. A statement just does something.

**Section** Getting started and first programs · **Level** 1 of 5 · **Time** about 10 minutes · **Status** hand written

## You will learn

- Expressions produce values such as `2 + 3`
- Statements do work such as `print(x)`
- Every statement is an expression, but not the other way round

## 1. Run the example

```bash
python 016-expressions/lesson_016_expressions.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_016_expressions.py</code></summary>

```python
"""Expressions.

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
```

</details>

## 3. Run the tests

```bash
pytest 016-expressions
```

## 4. Open the notebook

```bash
jupyter notebook 016-expressions/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `expression` | Code that produces a value |
| `statement` | A complete instruction |

## Your turn

1. Find three lines in your code that are expressions and three that are not.
2. Use `is_expression` on a file you wrote and see what it says.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/interpreter.html)

---

[← 015-assignment](../015-assignment/) · [Next: 017-statements →](../017-statements/)
