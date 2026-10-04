# 112 · UTF-8

Placeholder for **UTF-8**. A later phase replaces this with a full lesson.

**Section** Strings, encodings and regular expressions · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 112-utf8/lesson_112_utf8.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_112_utf8.py</code></summary>

```python
"""UTF-8.

Placeholder for **UTF-8**. A later phase replaces this with a full lesson.

Run me:
    python 112-utf8/lesson_112_utf8.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"utf8"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. UTF-8" for step in (1, 2, 3))


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
pytest 112-utf8
```

## 4. Open the notebook

```bash
jupyter notebook 112-utf8/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/strings.html)

---

[← 111-ascii](../111-ascii/) · [Next: 113-utf16 →](../113-utf16/)
