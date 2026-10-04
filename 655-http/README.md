# 655 · Http

`http` is a standard library module. This lesson shows how to look inside one.

**Section** Web concepts, scraping and security · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `http` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 655-http/lesson_655_http.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_655_http.py</code></summary>

```python
"""Http.

`http` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 655-http/lesson_655_http.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import http

    return getattr(http, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names http offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import http

    return sorted(item for item in dir(http) if not item.startswith("_"))


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
pytest 655-http
```

## 4. Open the notebook

```bash
jupyter notebook 655-http/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `http` | A standard library module for http |

## Your turn

1. Open the REPL, `import http`, then call `dir(http)`.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 654-urls](../654-urls/) · [Next: 656-https →](../656-https/)
