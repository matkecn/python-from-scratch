# 568 · Gzip

`gzip` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `gzip` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 568-gzip/lesson_568_gzip.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_568_gzip.py</code></summary>

```python
"""Gzip.

`gzip` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 568-gzip/lesson_568_gzip.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import gzip

    return getattr(gzip, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names gzip offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import gzip

    return sorted(item for item in dir(gzip) if not item.startswith("_"))


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
pytest 568-gzip
```

## 4. Open the notebook

```bash
jupyter notebook 568-gzip/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `gzip` | A standard library module for gzip |

## Your turn

1. Open the REPL, `import gzip`, then call `dir(gzip)`.

## Read more

- [`gzip` module docs](https://docs.python.org/3/library/gzip.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 567-zlib](../567-zlib/) · [Next: 569-bz2 →](../569-bz2/)
