# 311 · Context-managers

`with` sets something up and always tidies it away.

**Section** Decorators, context managers, descriptors and introspection · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- `with` opens and closes for you
- Safe even when the body raises
- Files, locks and sockets all use it

## 1. Run the example

```bash
python 311-context-managers/lesson_311_context_managers.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_311_context_managers.py</code></summary>

```python
"""Context-managers.

`with` sets something up and always tidies it away.

Run me:
    python 311-context-managers/lesson_311_context_managers.py
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
pytest 311-context-managers
```

## 4. Open the notebook

```bash
jupyter notebook 311-context-managers/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `context manager` | An object that sets up and tidies up |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 310-single-dispatch](../310-single-dispatch/) · [Next: 312-with →](../312-with/)
