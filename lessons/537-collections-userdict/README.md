# 537 · Collections-userdict

Placeholder for **Collections-userdict**. A later phase replaces this with a full lesson.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 537-collections-userdict/lesson_537_collections_userdict.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_537_collections_userdict.py</code></summary>

```python
"""Collections-userdict.

Placeholder for **Collections-userdict**. A later phase replaces this with a full lesson.

Run me:
    python 537-collections-userdict/lesson_537_collections_userdict.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"collections userdict"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Collections-userdict" for step in (1, 2, 3))


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
pytest 537-collections-userdict
```

## 4. Open the notebook

```bash
jupyter notebook 537-collections-userdict/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [`collections` module docs](https://docs.python.org/3/library/collections.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 536-collections-namedtuple](../536-collections-namedtuple/) · [Next: 538-collections-userlist →](../538-collections-userlist/)
