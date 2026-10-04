# 674 · Secrets

`secrets` is a standard library module. This lesson shows how to look inside one.

**Section** Web concepts, scraping and security · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `secrets` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 674-secrets/lesson_674_secrets.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_674_secrets.py</code></summary>

```python
"""Secrets.

`secrets` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 674-secrets/lesson_674_secrets.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import secrets

    return getattr(secrets, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names secrets offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import secrets

    return sorted(item for item in dir(secrets) if not item.startswith("_"))


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
pytest 674-secrets
```

## 4. Open the notebook

```bash
jupyter notebook 674-secrets/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `secrets` | A standard library module for secrets |

## Your turn

1. Open the REPL, `import secrets`, then call `dir(secrets)`.

## Read more

- [`secrets` module docs](https://docs.python.org/3/library/secrets.html)

---

[← 673-password-hashing](../673-password-hashing/) · [Next: 675-token-auth →](../675-token-auth/)
