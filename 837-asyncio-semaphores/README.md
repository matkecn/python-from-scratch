# 837 · Asyncio-semaphores

Placeholder for **Asyncio-semaphores**. A later phase replaces this with a full lesson.

**Section** Concurrency and asyncio · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 837-asyncio-semaphores/lesson_837_asyncio_semaphores.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_837_asyncio_semaphores.py</code></summary>

```python
"""Asyncio-semaphores.

Placeholder for **Asyncio-semaphores**. A later phase replaces this with a full lesson.

Run me:
    python 837-asyncio-semaphores/lesson_837_asyncio_semaphores.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"asyncio semaphores"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Asyncio-semaphores" for step in (1, 2, 3))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(outline())
    print(keywords())


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 837-asyncio-semaphores
```

## 4. Open the notebook

```bash
jupyter notebook 837-asyncio-semaphores/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [`asyncio` module docs](https://docs.python.org/3/library/asyncio.html)

---

[← 836-asyncio-events](../836-asyncio-events/) · [Next: 838-asyncio-streams →](../838-asyncio-streams/)
