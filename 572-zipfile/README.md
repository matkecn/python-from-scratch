# 572 · Zipfile

`zipfile` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `zipfile` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 572-zipfile/lesson_572_zipfile.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_572_zipfile.py</code></summary>

```python
"""Zipfile.

`zipfile` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 572-zipfile/lesson_572_zipfile.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import zipfile

    return getattr(zipfile, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names zipfile offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import zipfile

    return sorted(item for item in dir(zipfile) if not item.startswith("_"))


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
pytest 572-zipfile
```

## 4. Open the notebook

```bash
jupyter notebook 572-zipfile/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `zipfile` | A standard library module for zipfile |

## Your turn

1. Open the REPL, `import zipfile`, then call `dir(zipfile)`.

## Read more

- [`zipfile` module docs](https://docs.python.org/3/library/zipfile.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 571-tarfile](../571-tarfile/) · [Next: 573-archive-formats →](../573-archive-formats/)
