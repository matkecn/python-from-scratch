# 553 · Fileinput

`fileinput` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `fileinput` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 553-fileinput/lesson_553_fileinput.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_553_fileinput.py</code></summary>

```python
"""Fileinput.

`fileinput` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 553-fileinput/lesson_553_fileinput.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import fileinput

    return getattr(fileinput, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names fileinput offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import fileinput

    return sorted(item for item in dir(fileinput) if not item.startswith("_"))


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
pytest 553-fileinput
```

## 4. Open the notebook

```bash
jupyter notebook 553-fileinput/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `fileinput` | A standard library module for fileinput |

## Your turn

1. Open the REPL, `import fileinput`, then call `dir(fileinput)`.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 552-glob](../552-glob/) · [Next: 554-tempfile →](../554-tempfile/)
