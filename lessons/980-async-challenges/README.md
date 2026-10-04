# 980 · Async-challenges

`async` lets one program wait for many slow things at once.

**Section** Projects, challenges and mastery · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- `async def` makes a coroutine
- `await` waits without blocking
- `asyncio.gather` runs them together

## 1. Run the example

```bash
python 980-async-challenges/lesson_980_async_challenges.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_980_async_challenges.py</code></summary>

```python
"""Async-challenges.

`async` lets one program wait for many slow things at once.

Run me:
    python 980-async-challenges/lesson_980_async_challenges.py
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
pytest 980-async-challenges
```

## 4. Open the notebook

```bash
jupyter notebook 980-async-challenges/lesson.ipynb
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

[← 979-concurrency-challenges](../979-concurrency-challenges/) · [Next: 981-testing-challenges →](../981-testing-challenges/)
