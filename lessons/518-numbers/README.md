# 518 · Numbers

`numbers` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `numbers` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 518-numbers/lesson_518_numbers.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_518_numbers.py</code></summary>

```python
"""Numbers.

`numbers` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 518-numbers/lesson_518_numbers.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import numbers

    return getattr(numbers, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names numbers offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import numbers

    return sorted(item for item in dir(numbers) if not item.startswith("_"))


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
pytest 518-numbers
```

## 4. Open the notebook

```bash
jupyter notebook 518-numbers/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `numbers` | A standard library module for numbers |

## Your turn

1. Open the REPL, `import numbers`, then call `dir(numbers)`.

## Read more

- [`numbers` module docs](https://docs.python.org/3/library/numbers.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 517-statistics](../517-statistics/) · [Next: 519-matrix-basics →](../519-matrix-basics/)
