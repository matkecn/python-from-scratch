# 833 · Async-context-managers

`with` sets something up and always tidies it away.

**Section** Concurrency and asyncio · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- `with` opens and closes for you
- Safe even when the body raises
- Files, locks and sockets all use it

## 1. Run the example

```bash
python 833-async-context-managers/lesson_833_async_context_managers.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_833_async_context_managers.py</code></summary>

```python
"""Async-context-managers.

`with` sets something up and always tidies it away.

Run me:
    python 833-async-context-managers/lesson_833_async_context_managers.py
"""

from __future__ import annotations


from contextlib import contextmanager


@contextmanager
def announce(title: str):
    """Print a title before and after a block of code.

    Args:
        title: The title to print.

    Yields:
        The block to run.
    """
    print(f"start: {title}")
    yield
    print(f"end: {title}")


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    with announce("demo"):
        print("working")


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 833-async-context-managers
```

## 4. Open the notebook

```bash
jupyter notebook 833-async-context-managers/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `context manager` | An object that sets up and tidies up |

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 832-async-iterators](../832-async-iterators/) · [Next: 834-asyncio-queues →](../834-asyncio-queues/)
