# 813 · Queue

`queue` is a standard library module. This lesson shows how to look inside one.

**Section** Concurrency and asyncio · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `queue` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 813-queue/lesson_813_queue.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_813_queue.py</code></summary>

```python
"""Queue.

`queue` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 813-queue/lesson_813_queue.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import queue

    return getattr(queue, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names queue offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import queue

    return sorted(item for item in dir(queue) if not item.startswith("_"))


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
pytest 813-queue
```

## 4. Open the notebook

```bash
jupyter notebook 813-queue/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `queue` | A standard library module for queue |

## Your turn

1. Open the REPL, `import queue`, then call `dir(queue)`.

## Read more

- [`queue` module docs](https://docs.python.org/3/library/queue.html)

---

[← 812-barrier](../812-barrier/) · [Next: 814-producer-consumer →](../814-producer-consumer/)
