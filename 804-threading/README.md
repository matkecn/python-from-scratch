# 804 · Threading

`threading` is a standard library module. This lesson shows how to look inside one.

**Section** Concurrency and asyncio · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `threading` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 804-threading/lesson_804_threading.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_804_threading.py</code></summary>

```python
"""Threading.

`threading` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 804-threading/lesson_804_threading.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import threading

    return getattr(threading, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names threading offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import threading

    return sorted(item for item in dir(threading) if not item.startswith("_"))


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
pytest 804-threading
```

## 4. Open the notebook

```bash
jupyter notebook 804-threading/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `threading` | A standard library module for threading |

## Your turn

1. Open the REPL, `import threading`, then call `dir(threading)`.

## Read more

- [`threading` module docs](https://docs.python.org/3/library/threading.html)

---

[← 803-threads](../803-threads/) · [Next: 805-thread-pool →](../805-thread-pool/)
