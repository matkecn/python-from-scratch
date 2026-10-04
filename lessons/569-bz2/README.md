# 569 · Bz2

`bz2` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `bz2` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 569-bz2/lesson_569_bz2.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_569_bz2.py</code></summary>

```python
"""Bz2.

`bz2` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 569-bz2/lesson_569_bz2.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import bz2

    return getattr(bz2, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names bz2 offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import bz2

    return sorted(item for item in dir(bz2) if not item.startswith("_"))


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
pytest 569-bz2
```

## 4. Open the notebook

```bash
jupyter notebook 569-bz2/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `bz2` | A standard library module for bz2 |

## Your turn

1. Open the REPL, `import bz2`, then call `dir(bz2)`.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 568-gzip](../568-gzip/) · [Next: 570-lzma →](../570-lzma/)
