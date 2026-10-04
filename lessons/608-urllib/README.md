# 608 · Urllib

`urllib` is a standard library module. This lesson shows how to look inside one.

**Section** Networking, APIs and databases · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `urllib` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 608-urllib/lesson_608_urllib.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_608_urllib.py</code></summary>

```python
"""Urllib.

`urllib` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 608-urllib/lesson_608_urllib.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import urllib

    return getattr(urllib, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names urllib offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import urllib

    return sorted(item for item in dir(urllib) if not item.startswith("_"))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(module_path())
    print(len(public_names()), 'public names')


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 608-urllib
```

## 4. Open the notebook

```bash
jupyter notebook 608-urllib/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `urllib` | A standard library module for urllib |

## Your turn

1. Open the REPL, `import urllib`, then call `dir(urllib)`.

## Read more

- [`urllib` module docs](https://docs.python.org/3/library/urllib.html)

---

[← 607-http-basics](../607-http-basics/) · [Next: 609-http-client →](../609-http-client/)
