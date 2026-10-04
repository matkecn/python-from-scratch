# 017 · Statements

One instruction per line. Python reads top to bottom.

**Section** Getting started and first programs · **Level** 1 of 5 · **Time** about 10 minutes · **Status** hand written

## You will learn

- A statement is a complete instruction
- Lines run from the top down
- Indentation changes what a line belongs to

## 1. Run the example

```bash
python 017-statements/lesson_017_statements.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_017_statements.py</code></summary>

```python
"""Statements.

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
```

</details>

## 3. Run the tests

```bash
pytest 017-statements
```

## 4. Open the notebook

```bash
jupyter notebook 017-statements/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `statement` | One complete instruction |
| `program flow` | The order instructions run in |

## Your turn

1. Count the statements in a file you wrote.
2. Predict the output of a five line program, then run it to check.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/interpreter.html)

---

[← 016-expressions](../016-expressions/) · [Next: 018-keywords →](../018-keywords/)
