# 609 · Http-client

Placeholder for **Http-client**. A later phase replaces this with a full lesson.

**Section** Networking, APIs and databases · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 609-http-client/lesson_609_http_client.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_609_http_client.py</code></summary>

```python
"""Http-client.

Placeholder for **Http-client**. A later phase replaces this with a full lesson.

Run me:
    python 609-http-client/lesson_609_http_client.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"http client"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Http-client" for step in (1, 2, 3))


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
pytest 609-http-client
```

## 4. Open the notebook

```bash
jupyter notebook 609-http-client/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 608-urllib](../608-urllib/) · [Next: 610-http-server →](../610-http-server/)
