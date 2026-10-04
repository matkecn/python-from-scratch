# 245 · Weakref

`weakref` is a standard library module. This lesson shows how to look inside one.

**Section** Object oriented programming · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `weakref` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 245-weakref/lesson_245_weakref.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_245_weakref.py</code></summary>

```python
"""Weakref.

`weakref` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 245-weakref/lesson_245_weakref.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import weakref

    return getattr(weakref, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names weakref offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import weakref

    return sorted(item for item in dir(weakref) if not item.startswith("_"))


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
pytest 245-weakref
```

## 4. Open the notebook

```bash
jupyter notebook 245-weakref/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `weakref` | A standard library module for weakref |

## Your turn

1. Open the REPL, `import weakref`, then call `dir(weakref)`.

## Read more

- [`weakref` module docs](https://docs.python.org/3/library/weakref.html)
- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 244-reference-counting](../244-reference-counting/) · [Next: 246-slots →](../246-slots/)
