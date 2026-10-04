# 175 · Importlib

`importlib` is a standard library module. This lesson shows how to look inside one.

**Section** Modules, imports and exceptions · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `importlib` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 175-importlib/lesson_175_importlib.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_175_importlib.py</code></summary>

```python
"""Importlib.

`importlib` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 175-importlib/lesson_175_importlib.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import importlib

    return getattr(importlib, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names importlib offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import importlib

    return sorted(item for item in dir(importlib) if not item.startswith("_"))


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
pytest 175-importlib
```

## 4. Open the notebook

```bash
jupyter notebook 175-importlib/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `importlib` | A standard library module for importlib |

## Your turn

1. Open the REPL, `import importlib`, then call `dir(importlib)`.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 174-module-reloading](../174-module-reloading/) · [Next: 176-module-specs →](../176-module-specs/)
