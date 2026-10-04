# 492 · Shelve

`shelve` is a standard library module. This lesson shows how to look inside one.

**Section** Files, paths and serialization · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `shelve` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 492-shelve/lesson_492_shelve.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_492_shelve.py</code></summary>

```python
"""Shelve.

`shelve` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 492-shelve/lesson_492_shelve.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import shelve

    return getattr(shelve, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names shelve offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import shelve

    return sorted(item for item in dir(shelve) if not item.startswith("_"))


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
pytest 492-shelve
```

## 4. Open the notebook

```bash
jupyter notebook 492-shelve/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `shelve` | A standard library module for shelve |

## Your turn

1. Open the REPL, `import shelve`, then call `dir(shelve)`.

## Read more

- [`shelve` module docs](https://docs.python.org/3/library/shelve.html)
- [official tutorial](https://docs.python.org/3/tutorial/inputoutput.html)

---

[← 491-pickle-security](../491-pickle-security/) · [Next: 493-configparser →](../493-configparser/)
