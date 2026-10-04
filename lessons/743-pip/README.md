# 743 · Pip

Placeholder for **Pip**. A later phase replaces this with a full lesson.

**Section** Packaging, style, CI and documentation · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 743-pip/lesson_743_pip.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_743_pip.py</code></summary>

```python
"""Pip.

Placeholder for **Pip**. A later phase replaces this with a full lesson.

Run me:
    python 743-pip/lesson_743_pip.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"pip"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Pip" for step in (1, 2, 3))


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
pytest 743-pip
```

## 4. Open the notebook

```bash
jupyter notebook 743-pip/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 742-venv](../742-venv/) · [Next: 744-pip-install →](../744-pip-install/)
