# 816 · Multiprocessing

`multiprocessing` is a standard library module. This lesson shows how to look inside one.

**Section** Concurrency and asyncio · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `multiprocessing` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 816-multiprocessing/lesson_816_multiprocessing.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_816_multiprocessing.py</code></summary>

```python
"""Multiprocessing.

`multiprocessing` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 816-multiprocessing/lesson_816_multiprocessing.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import multiprocessing

    return getattr(multiprocessing, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names multiprocessing offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import multiprocessing

    return sorted(item for item in dir(multiprocessing) if not item.startswith("_"))


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
pytest 816-multiprocessing
```

## 4. Open the notebook

```bash
jupyter notebook 816-multiprocessing/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `multiprocessing` | A standard library module for multiprocessing |

## Your turn

1. Open the REPL, `import multiprocessing`, then call `dir(multiprocessing)`.

## Read more

- [`multiprocessing` module docs](https://docs.python.org/3/library/multiprocessing.html)

---

[← 815-threading-project](../815-threading-project/) · [Next: 817-process-pool →](../817-process-pool/)
