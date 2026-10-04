# 648 · Ftp

Placeholder for **Ftp**. A later phase replaces this with a full lesson.

**Section** Networking, APIs and databases · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 648-ftp/lesson_648_ftp.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_648_ftp.py</code></summary>

```python
"""Ftp.

Placeholder for **Ftp**. A later phase replaces this with a full lesson.

Run me:
    python 648-ftp/lesson_648_ftp.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"ftp"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Ftp" for step in (1, 2, 3))


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
pytest 648-ftp
```

## 4. Open the notebook

```bash
jupyter notebook 648-ftp/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 647-email-project](../647-email-project/) · [Next: 649-telnet →](../649-telnet/)
