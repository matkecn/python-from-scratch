# 221 · Abc

`abc` is a standard library module. This lesson shows how to look inside one.

**Section** Object oriented programming · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `abc` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 221-abc/lesson_221_abc.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_221_abc.py</code></summary>

```python
"""Abc.

`abc` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 221-abc/lesson_221_abc.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import abc

    return getattr(abc, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names abc offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import abc

    return sorted(item for item in dir(abc) if not item.startswith("_"))


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
pytest 221-abc
```

## 4. Open the notebook

```bash
jupyter notebook 221-abc/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `abc` | A standard library module for abc |

## Your turn

1. Open the REPL, `import abc`, then call `dir(abc)`.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 220-abstraction](../220-abstraction/) · [Next: 222-abstractmethod →](../222-abstractmethod/)
