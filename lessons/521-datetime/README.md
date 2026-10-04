# 521 · Datetime

`datetime` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `datetime` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 521-datetime/lesson_521_datetime.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_521_datetime.py</code></summary>

```python
"""Datetime.

`datetime` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 521-datetime/lesson_521_datetime.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import datetime

    return getattr(datetime, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names datetime offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import datetime

    return sorted(item for item in dir(datetime) if not item.startswith("_"))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(module_path())
    print(len(public_names()), 'public names')


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 521-datetime
```

## 4. Open the notebook

```bash
jupyter notebook 521-datetime/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `datetime` | A standard library module for datetime |

## Your turn

1. Open the REPL, `import datetime`, then call `dir(datetime)`.

## Read more

- [`datetime` module docs](https://docs.python.org/3/library/datetime.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 520-numeric-project](../520-numeric-project/) · [Next: 522-date →](../522-date/)
