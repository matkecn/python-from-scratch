# 699 · Monitoring basics

Placeholder for **Monitoring basics**. A later phase replaces this with a full lesson.

**Section** Web concepts, scraping and security · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 699-monitoring-basics/lesson_699_monitoring_basics.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_699_monitoring_basics.py</code></summary>

```python
"""Monitoring basics.

Placeholder for **Monitoring basics**. A later phase replaces this with a full lesson.

Run me:
    python 699-monitoring-basics/lesson_699_monitoring_basics.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"monitoring basics"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Monitoring basics" for step in (1, 2, 3))


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
pytest 699-monitoring-basics
```

## 4. Open the notebook

```bash
jupyter notebook 699-monitoring-basics/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 698-service-health](../698-service-health/) · [Next: 700-networking-capstone →](../700-networking-capstone/)
