# 641 · Email

`email` is a standard library module. This lesson shows how to look inside one.

**Section** Networking, APIs and databases · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `email` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 641-email/lesson_641_email.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_641_email.py</code></summary>

```python
"""Email.

`email` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 641-email/lesson_641_email.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import email

    return getattr(email, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names email offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import email

    return sorted(item for item in dir(email) if not item.startswith("_"))


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
pytest 641-email
```

## 4. Open the notebook

```bash
jupyter notebook 641-email/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `email` | A standard library module for email |

## Your turn

1. Open the REPL, `import email`, then call `dir(email)`.

## Read more

- [`email` module docs](https://docs.python.org/3/library/email.html)

---

[← 640-database-project](../640-database-project/) · [Next: 642-smtp →](../642-smtp/)
