# 897 · Async-internals

`async` lets one program wait for many slow things at once.

**Section** Performance, memory and CPython internals · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- `async def` makes a coroutine
- `await` waits without blocking
- `asyncio.gather` runs them together

## 1. Run the example

```bash
python 897-async-internals/lesson_897_async_internals.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_897_async_internals.py</code></summary>

```python
"""Async-internals.

`async` lets one program wait for many slow things at once.

Run me:
    python 897-async-internals/lesson_897_async_internals.py
"""

from __future__ import annotations


import asyncio


async def double(number: int) -> int:
    """Double a number after a tiny pause.

    Args:
        number: The number to double.

    Returns:
        The doubled number.
    """
    await asyncio.sleep(0)
    return number * 2


async def double_all(numbers: list[int]) -> list[int]:
    """Double many numbers at the same time.

    Args:
        numbers: The numbers to double.

    Returns:
        The doubled numbers, in order.
    """
    return list(await asyncio.gather(*(double(number) for number in numbers)))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    import asyncio

    print(asyncio.run(double_all([1, 2, 3])))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 897-async-internals
```

## 4. Open the notebook

```bash
jupyter notebook 897-async-internals/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `coroutine` | A function that waits using `await` |
| `event loop` | The scheduler that runs waiting code |

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 896-thread-internals](../896-thread-internals/) · [Next: 898-performance-internals →](../898-performance-internals/)
