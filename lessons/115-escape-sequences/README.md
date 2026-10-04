# 115 · Escape-sequences

Placeholder for **Escape-sequences**. A later phase replaces this with a full lesson.

**Section** Strings, encodings and regular expressions · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 115-escape-sequences/lesson_115_escape_sequences.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_115_escape_sequences.py</code></summary>

```python
"""Escape-sequences.

Placeholder for **Escape-sequences**. A later phase replaces this with a full lesson.

Run me:
    python 115-escape-sequences/lesson_115_escape_sequences.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"escape sequences"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Escape-sequences" for step in (1, 2, 3))


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
pytest 115-escape-sequences
```

## 4. Open the notebook

```bash
jupyter notebook 115-escape-sequences/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/strings.html)

---

[← 114-utf32](../114-utf32/) · [Next: 116-regex-introduction →](../116-regex-introduction/)
