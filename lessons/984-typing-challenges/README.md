# 984 · Typing-challenges

Placeholder for **Typing-challenges**. A later phase replaces this with a full lesson.

**Section** Projects, challenges and mastery · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 984-typing-challenges/lesson_984_typing_challenges.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_984_typing_challenges.py</code></summary>

```python
"""Typing-challenges.

Placeholder for **Typing-challenges**. A later phase replaces this with a full lesson.

Run me:
    python 984-typing-challenges/lesson_984_typing_challenges.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"typing challenges"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Typing-challenges" for step in (1, 2, 3))


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
pytest 984-typing-challenges
```

## 4. Open the notebook

```bash
jupyter notebook 984-typing-challenges/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [`typing` module docs](https://docs.python.org/3/library/typing.html)

---

[← 983-performance-challenges](../983-performance-challenges/) · [Next: 985-metaprogramming-challenges →](../985-metaprogramming-challenges/)
