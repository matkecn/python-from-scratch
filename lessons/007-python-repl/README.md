# 007 · Python-repl

The REPL is a Python prompt that answers straight away.

**Section** Getting started and first programs · **Level** 1 of 5 · **Time** about 10 minutes · **Status** hand written

## You will learn

- Know the four parts of the prompt
- Try an expression and see the value
- Keep a useful line in your history

## 1. Run the example

```bash
python 007-python-repl/lesson_007_python_repl.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_007_python_repl.py</code></summary>

```python
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
```

</details>

## 3. Run the tests

```bash
pytest 007-python-repl
```

## 4. Open the notebook

```bash
jupyter notebook 007-python-repl/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `REPL` | Read, Evaluate, Print, Loop: the interactive prompt |
| `expression` | A piece of code that produces a value |

## Your turn

1. Start the REPL with `python3` and try `2 ** 100`.
2. Find the difference between `2/1` and `2//1` in the prompt.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/interpreter.html)

---

[← 006-running-python](../006-running-python/) · [Next: 008-python-files →](../008-python-files/)
