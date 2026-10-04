# 571 · Tarfile

`tarfile` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `tarfile` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 571-tarfile/lesson_571_tarfile.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_571_tarfile.py</code></summary>

```python
"""Tarfile.

`tarfile` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 571-tarfile/lesson_571_tarfile.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import tarfile

    return getattr(tarfile, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names tarfile offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import tarfile

    return sorted(item for item in dir(tarfile) if not item.startswith("_"))


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
pytest 571-tarfile
```

## 4. Open the notebook

```bash
jupyter notebook 571-tarfile/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `tarfile` | A standard library module for tarfile |

## Your turn

1. Open the REPL, `import tarfile`, then call `dir(tarfile)`.

## Read more

- [`tarfile` module docs](https://docs.python.org/3/library/tarfile.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 570-lzma](../570-lzma/) · [Next: 572-zipfile →](../572-zipfile/)
