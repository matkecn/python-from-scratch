# 318 · Contextlib

`contextlib` is a standard library module. This lesson shows how to look inside one.

**Section** Decorators, context managers, descriptors and introspection · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `contextlib` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 318-contextlib/lesson_318_contextlib.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_318_contextlib.py</code></summary>

```python
"""Contextlib.

`contextlib` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 318-contextlib/lesson_318_contextlib.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import contextlib

    return getattr(contextlib, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names contextlib offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import contextlib

    return sorted(item for item in dir(contextlib) if not item.startswith("_"))


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
pytest 318-contextlib
```

## 4. Open the notebook

```bash
jupyter notebook 318-contextlib/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `contextlib` | A standard library module for contextlib |

## Your turn

1. Open the REPL, `import contextlib`, then call `dir(contextlib)`.

## Read more

- [`contextlib` module docs](https://docs.python.org/3/library/contextlib.html)
- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 317-custom-context-managers](../317-custom-context-managers/) · [Next: 319-contextlib-suppress →](../319-contextlib-suppress/)
