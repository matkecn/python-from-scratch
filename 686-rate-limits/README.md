# 686 · Rate-limits

Placeholder for **Rate-limits**. A later phase replaces this with a full lesson.

**Section** Web concepts, scraping and security · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 686-rate-limits/lesson_686_rate_limits.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_686_rate_limits.py</code></summary>

```python
"""Rate-limits.

Placeholder for **Rate-limits**. A later phase replaces this with a full lesson.

Run me:
    python 686-rate-limits/lesson_686_rate_limits.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"rate limits"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Rate-limits" for step in (1, 2, 3))


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
pytest 686-rate-limits
```

## 4. Open the notebook

```bash
jupyter notebook 686-rate-limits/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 685-backoff](../685-backoff/) · [Next: 687-api-pagination →](../687-api-pagination/)
