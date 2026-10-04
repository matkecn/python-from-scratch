# 945 · Report-generation

Placeholder for **Report-generation**. A later phase replaces this with a full lesson.

**Section** Practical Python applications · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 945-report-generation/lesson_945_report_generation.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_945_report_generation.py</code></summary>

```python
"""Report-generation.

Placeholder for **Report-generation**. A later phase replaces this with a full lesson.

Run me:
    python 945-report-generation/lesson_945_report_generation.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"report generation"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Report-generation" for step in (1, 2, 3))


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
pytest 945-report-generation
```

## 4. Open the notebook

```bash
jupyter notebook 945-report-generation/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 944-web-automation](../944-web-automation/) · [Next: 946-scheduled-scripts →](../946-scheduled-scripts/)
