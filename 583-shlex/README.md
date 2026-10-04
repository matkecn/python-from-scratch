# 583 · Shlex

`shlex` is a standard library module. This lesson shows how to look inside one.

**Section** Command line tools and logging · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `shlex` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 583-shlex/lesson_583_shlex.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_583_shlex.py</code></summary>

```python
"""Shlex.

`shlex` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 583-shlex/lesson_583_shlex.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import shlex

    return getattr(shlex, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names shlex offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import shlex

    return sorted(item for item in dir(shlex) if not item.startswith("_"))


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
pytest 583-shlex
```

## 4. Open the notebook

```bash
jupyter notebook 583-shlex/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `shlex` | A standard library module for shlex |

## Your turn

1. Open the REPL, `import shlex`, then call `dir(shlex)`.

## Read more

- [`shlex` module docs](https://docs.python.org/3/library/shlex.html)

---

[← 582-getopt](../582-getopt/) · [Next: 584-cli-arguments →](../584-cli-arguments/)
