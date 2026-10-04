# 546 · Textwrap

`textwrap` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `textwrap` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 546-textwrap/lesson_546_textwrap.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_546_textwrap.py</code></summary>

```python
"""Textwrap.

`textwrap` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 546-textwrap/lesson_546_textwrap.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import textwrap

    return getattr(textwrap, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names textwrap offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import textwrap

    return sorted(item for item in dir(textwrap) if not item.startswith("_"))


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
pytest 546-textwrap
```

## 4. Open the notebook

```bash
jupyter notebook 546-textwrap/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `textwrap` | A standard library module for textwrap |

## Your turn

1. Open the REPL, `import textwrap`, then call `dir(textwrap)`.

## Read more

- [`textwrap` module docs](https://docs.python.org/3/library/textwrap.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 545-pprint](../545-pprint/) · [Next: 547-string →](../547-string/)
