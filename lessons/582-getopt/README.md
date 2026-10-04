# 582 · Getopt

`getopt` is a standard library module. This lesson shows how to look inside one.

**Section** Command line tools and logging · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `getopt` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 582-getopt/lesson_582_getopt.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_582_getopt.py</code></summary>

```python
"""Getopt.

`getopt` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 582-getopt/lesson_582_getopt.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import getopt

    return getattr(getopt, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names getopt offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import getopt

    return sorted(item for item in dir(getopt) if not item.startswith("_"))


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
pytest 582-getopt
```

## 4. Open the notebook

```bash
jupyter notebook 582-getopt/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `getopt` | A standard library module for getopt |

## Your turn

1. Open the REPL, `import getopt`, then call `dir(getopt)`.

## Read more

- [`getopt` module docs](https://docs.python.org/3/library/getopt.html)

---

[← 581-argparse](../581-argparse/) · [Next: 583-shlex →](../583-shlex/)
