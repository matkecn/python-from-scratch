# 431 · Sequence-protocol

Placeholder for **Sequence-protocol**. A later phase replaces this with a full lesson.

**Section** The Python data model (dunder methods) · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 431-sequence-protocol/lesson_431_sequence_protocol.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_431_sequence_protocol.py</code></summary>

```python
"""Sequence-protocol.

Placeholder for **Sequence-protocol**. A later phase replaces this with a full lesson.

Run me:
    python 431-sequence-protocol/lesson_431_sequence_protocol.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"sequence protocol"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Sequence-protocol" for step in (1, 2, 3))


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
pytest 431-sequence-protocol
```

## 4. Open the notebook

```bash
jupyter notebook 431-sequence-protocol/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/datamodel.html)

---

[← 430-container-protocol](../430-container-protocol/) · [Next: 432-mapping-protocol →](../432-mapping-protocol/)
