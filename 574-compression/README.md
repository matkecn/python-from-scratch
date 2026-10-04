# 574 · Compression

`compression` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `compression` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 574-compression/lesson_574_compression.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_574_compression.py</code></summary>

```python
"""Compression.

`compression` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 574-compression/lesson_574_compression.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import compression

    return getattr(compression, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names compression offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import compression

    return sorted(item for item in dir(compression) if not item.startswith("_"))


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
pytest 574-compression
```

## 4. Open the notebook

```bash
jupyter notebook 574-compression/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `compression` | A standard library module for compression |

## Your turn

1. Open the REPL, `import compression`, then call `dir(compression)`.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 573-archive-formats](../573-archive-formats/) · [Next: 575-file-archives →](../575-file-archives/)
