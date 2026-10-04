# 644 · Email-attachments

Placeholder for **Email-attachments**. A later phase replaces this with a full lesson.

**Section** Networking, APIs and databases · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 644-email-attachments/lesson_644_email_attachments.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_644_email_attachments.py</code></summary>

```python
"""Email-attachments.

Placeholder for **Email-attachments**. A later phase replaces this with a full lesson.

Run me:
    python 644-email-attachments/lesson_644_email_attachments.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"email attachments"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Email-attachments" for step in (1, 2, 3))


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
pytest 644-email-attachments
```

## 4. Open the notebook

```bash
jupyter notebook 644-email-attachments/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [`email` module docs](https://docs.python.org/3/library/email.html)

---

[← 643-email-messages](../643-email-messages/) · [Next: 645-email-parsing →](../645-email-parsing/)
