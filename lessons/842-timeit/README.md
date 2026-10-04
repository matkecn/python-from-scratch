# 842 · Timeit

`timeit` is a standard library module. This lesson shows how to look inside one.

**Section** Performance, memory and CPython internals · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `timeit` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 842-timeit/lesson_842_timeit.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_842_timeit.py</code></summary>

```python
"""Timeit.

`timeit` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 842-timeit/lesson_842_timeit.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import timeit

    return getattr(timeit, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names timeit offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import timeit

    return sorted(item for item in dir(timeit) if not item.startswith("_"))


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
pytest 842-timeit
```

## 4. Open the notebook

```bash
jupyter notebook 842-timeit/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `timeit` | A standard library module for timeit |

## Your turn

1. Open the REPL, `import timeit`, then call `dir(timeit)`.

## Read more

- [`timeit` module docs](https://docs.python.org/3/library/timeit.html)

---

[← 841-performance](../841-performance/) · [Next: 843-profiling →](../843-profiling/)
