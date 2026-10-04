# 113 · UTF-16

Placeholder for **UTF-16**. A later phase replaces this with a full lesson.

**Section** Strings, encodings and regular expressions · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 113-utf16/lesson_113_utf16.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_113_utf16.py</code></summary>

```python
"""UTF-16.

Placeholder for **UTF-16**. A later phase replaces this with a full lesson.

Run me:
    python 113-utf16/lesson_113_utf16.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"utf16"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. UTF-16" for step in (1, 2, 3))


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
pytest 113-utf16
```

## 4. Open the notebook

```bash
jupyter notebook 113-utf16/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/strings.html)

---

[← 112-utf8](../112-utf8/) · [Next: 114-utf32 →](../114-utf32/)
