# 019 · Builtins

Built in functions come with Python. You do not have to write them.

**Section** Getting started and first programs · **Level** 1 of 5 · **Time** about 10 minutes · **Status** hand written

## You will learn

- `len`, `sum`, `min` and `max` are always there
- `dir` shows what an object can do
- `help` explains anything

## 1. Run the example

```bash
python 019-builtins/lesson_019_builtins.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_019_builtins.py</code></summary>

```python
"""Builtins.

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
```

</details>

## 3. Run the tests

```bash
pytest 019-builtins
```

## 4. Open the notebook

```bash
jupyter notebook 019-builtins/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `built in` | Something Python gives you without importing |
| `namespace` | The names Python knows at the moment |

## Your turn

1. Find three built in functions you did not know and use them today.
2. Use `help` on `sorted` and read the first line it prints.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/interpreter.html)

---

[← 018-keywords](../018-keywords/) · [Next: 020-first-program →](../020-first-program/)
