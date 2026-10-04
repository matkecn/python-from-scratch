# 570 · Lzma

`lzma` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `lzma` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 570-lzma/lesson_570_lzma.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_570_lzma.py</code></summary>

```python
"""Lzma.

`lzma` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 570-lzma/lesson_570_lzma.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import lzma

    return getattr(lzma, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names lzma offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import lzma

    return sorted(item for item in dir(lzma) if not item.startswith("_"))


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
pytest 570-lzma
```

## 4. Open the notebook

```bash
jupyter notebook 570-lzma/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `lzma` | A standard library module for lzma |

## Your turn

1. Open the REPL, `import lzma`, then call `dir(lzma)`.

## Read more

- [`lzma` module docs](https://docs.python.org/3/library/lzma.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 569-bz2](../569-bz2/) · [Next: 571-tarfile →](../571-tarfile/)
