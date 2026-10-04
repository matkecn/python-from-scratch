# 555 · Io

`io` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `io` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 555-io/lesson_555_io.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_555_io.py</code></summary>

```python
"""Io.

`io` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 555-io/lesson_555_io.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import io

    return getattr(io, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names io offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import io

    return sorted(item for item in dir(io) if not item.startswith("_"))


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
pytest 555-io
```

## 4. Open the notebook

```bash
jupyter notebook 555-io/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `io` | A standard library module for io |

## Your turn

1. Open the REPL, `import io`, then call `dir(io)`.

## Read more

- [`io` module docs](https://docs.python.org/3/library/io.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 554-tempfile](../554-tempfile/) · [Next: 556-logging →](../556-logging/)
