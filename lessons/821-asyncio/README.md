# 821 · Asyncio

`asyncio` is a standard library module. This lesson shows how to look inside one.

**Section** Concurrency and asyncio · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `asyncio` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 821-asyncio/lesson_821_asyncio.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_821_asyncio.py</code></summary>

```python
"""Asyncio.

`asyncio` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 821-asyncio/lesson_821_asyncio.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import asyncio

    return getattr(asyncio, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names asyncio offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import asyncio

    return sorted(item for item in dir(asyncio) if not item.startswith("_"))


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
pytest 821-asyncio
```

## 4. Open the notebook

```bash
jupyter notebook 821-asyncio/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `asyncio` | A standard library module for asyncio |

## Your turn

1. Open the REPL, `import asyncio`, then call `dir(asyncio)`.

## Read more

- [`asyncio` module docs](https://docs.python.org/3/library/asyncio.html)

---

[← 820-multiprocessing-project](../820-multiprocessing-project/) · [Next: 822-event-loop →](../822-event-loop/)
