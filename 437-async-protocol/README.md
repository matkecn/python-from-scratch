# 437 · Async-protocol

`async` lets one program wait for many slow things at once.

**Section** The Python data model (dunder methods) · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- `async def` makes a coroutine
- `await` waits without blocking
- `asyncio.gather` runs them together

## 1. Run the example

```bash
python 437-async-protocol/lesson_437_async_protocol.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_437_async_protocol.py</code></summary>

```python
"""Async-protocol.

`async` lets one program wait for many slow things at once.

Run me:
    python 437-async-protocol/lesson_437_async_protocol.py
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
pytest 437-async-protocol
```

## 4. Open the notebook

```bash
jupyter notebook 437-async-protocol/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `coroutine` | A function that waits using `await` |
| `event loop` | The scheduler that runs waiting code |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/datamodel.html)

---

[← 436-descriptor-protocol](../436-descriptor-protocol/) · [Next: 438-awaitable →](../438-awaitable/)
