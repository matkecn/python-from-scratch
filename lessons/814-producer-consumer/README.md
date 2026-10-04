# 814 · Producer-consumer

Placeholder for **Producer-consumer**. A later phase replaces this with a full lesson.

**Section** Concurrency and asyncio · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 814-producer-consumer/lesson_814_producer_consumer.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_814_producer_consumer.py</code></summary>

```python
"""Producer-consumer.

Placeholder for **Producer-consumer**. A later phase replaces this with a full lesson.

Run me:
    python 814-producer-consumer/lesson_814_producer_consumer.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"producer consumer"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Producer-consumer" for step in (1, 2, 3))


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
pytest 814-producer-consumer
```

## 4. Open the notebook

```bash
jupyter notebook 814-producer-consumer/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 813-queue](../813-queue/) · [Next: 815-threading-project →](../815-threading-project/)
