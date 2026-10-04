# 447 · Custom-context-manager

`with` sets something up and always tidies it away.

**Section** The Python data model (dunder methods) · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- `with` opens and closes for you
- Safe even when the body raises
- Files, locks and sockets all use it

## 1. Run the example

```bash
python 447-custom-context-manager/lesson_447_custom_context_manager.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_447_custom_context_manager.py</code></summary>

```python
"""Custom-context-manager.

`with` sets something up and always tidies it away.

Run me:
    python 447-custom-context-manager/lesson_447_custom_context_manager.py
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
pytest 447-custom-context-manager
```

## 4. Open the notebook

```bash
jupyter notebook 447-custom-context-manager/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `context manager` | An object that sets up and tidies up |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/datamodel.html)

---

[← 446-custom-iterator](../446-custom-iterator/) · [Next: 448-custom-awaitable →](../448-custom-awaitable/)
