# 554 · Tempfile

`tempfile` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `tempfile` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 554-tempfile/lesson_554_tempfile.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_554_tempfile.py</code></summary>

```python
"""Tempfile.

`tempfile` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 554-tempfile/lesson_554_tempfile.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import tempfile

    return getattr(tempfile, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names tempfile offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import tempfile

    return sorted(item for item in dir(tempfile) if not item.startswith("_"))


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
pytest 554-tempfile
```

## 4. Open the notebook

```bash
jupyter notebook 554-tempfile/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `tempfile` | A standard library module for tempfile |

## Your turn

1. Open the REPL, `import tempfile`, then call `dir(tempfile)`.

## Read more

- [`tempfile` module docs](https://docs.python.org/3/library/tempfile.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 553-fileinput](../553-fileinput/) · [Next: 555-io →](../555-io/)
