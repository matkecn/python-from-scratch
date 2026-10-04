# 592 · Log-levels

Placeholder for **Log-levels**. A later phase replaces this with a full lesson.

**Section** Command line tools and logging · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 592-log-levels/lesson_592_log_levels.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_592_log_levels.py</code></summary>

```python
"""Log-levels.

Placeholder for **Log-levels**. A later phase replaces this with a full lesson.

Run me:
    python 592-log-levels/lesson_592_log_levels.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"log levels"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Log-levels" for step in (1, 2, 3))


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
pytest 592-log-levels
```

## 4. Open the notebook

```bash
jupyter notebook 592-log-levels/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 591-logging-basics](../591-logging-basics/) · [Next: 593-loggers →](../593-loggers/)
