# 849 · Tracemalloc

`tracemalloc` is a standard library module. This lesson shows how to look inside one.

**Section** Performance, memory and CPython internals · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `tracemalloc` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 849-tracemalloc/lesson_849_tracemalloc.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_849_tracemalloc.py</code></summary>

```python
"""Tracemalloc.

`tracemalloc` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 849-tracemalloc/lesson_849_tracemalloc.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import tracemalloc

    return getattr(tracemalloc, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names tracemalloc offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import tracemalloc

    return sorted(item for item in dir(tracemalloc) if not item.startswith("_"))


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
pytest 849-tracemalloc
```

## 4. Open the notebook

```bash
jupyter notebook 849-tracemalloc/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `tracemalloc` | A standard library module for tracemalloc |

## Your turn

1. Open the REPL, `import tracemalloc`, then call `dir(tracemalloc)`.

## Read more

- [`tracemalloc` module docs](https://docs.python.org/3/library/tracemalloc.html)

---

[← 848-memory-profiling](../848-memory-profiling/) · [Next: 850-performance-project →](../850-performance-project/)
