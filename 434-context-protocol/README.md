# 434 · Context-protocol

Placeholder for **Context-protocol**. A later phase replaces this with a full lesson.

**Section** The Python data model (dunder methods) · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 434-context-protocol/lesson_434_context_protocol.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_434_context_protocol.py</code></summary>

```python
"""Context-protocol.

Placeholder for **Context-protocol**. A later phase replaces this with a full lesson.

Run me:
    python 434-context-protocol/lesson_434_context_protocol.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"context protocol"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Context-protocol" for step in (1, 2, 3))


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
pytest 434-context-protocol
```

## 4. Open the notebook

```bash
jupyter notebook 434-context-protocol/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/datamodel.html)

---

[← 433-callable-objects](../433-callable-objects/) · [Next: 435-iterator-protocol →](../435-iterator-protocol/)
