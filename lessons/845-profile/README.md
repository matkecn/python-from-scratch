# 845 · Profile

`profile` is a standard library module. This lesson shows how to look inside one.

**Section** Performance, memory and CPython internals · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `profile` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 845-profile/lesson_845_profile.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_845_profile.py</code></summary>

```python
"""Profile.

`profile` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 845-profile/lesson_845_profile.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import profile

    return getattr(profile, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names profile offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import profile

    return sorted(item for item in dir(profile) if not item.startswith("_"))


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
pytest 845-profile
```

## 4. Open the notebook

```bash
jupyter notebook 845-profile/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `profile` | A standard library module for profile |

## Your turn

1. Open the REPL, `import profile`, then call `dir(profile)`.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 844-cprofile](../844-cprofile/) · [Next: 846-pstats →](../846-pstats/)
