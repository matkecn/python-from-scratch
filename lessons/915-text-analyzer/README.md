# 915 · Text-analyzer

Placeholder for **Text-analyzer**. A later phase replaces this with a full lesson.

**Section** Practical Python applications · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 915-text-analyzer/lesson_915_text_analyzer.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_915_text_analyzer.py</code></summary>

```python
"""Text-analyzer.

Placeholder for **Text-analyzer**. A later phase replaces this with a full lesson.

Run me:
    python 915-text-analyzer/lesson_915_text_analyzer.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"text analyzer"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Text-analyzer" for step in (1, 2, 3))


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
pytest 915-text-analyzer
```

## 4. Open the notebook

```bash
jupyter notebook 915-text-analyzer/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 914-log-parser](../914-log-parser/) · [Next: 916-file-organizer →](../916-file-organizer/)
