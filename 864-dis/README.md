# 864 · Dis

`dis` is a standard library module. This lesson shows how to look inside one.

**Section** Performance, memory and CPython internals · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `dis` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 864-dis/lesson_864_dis.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_864_dis.py</code></summary>

```python
"""Dis.

`dis` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 864-dis/lesson_864_dis.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import dis

    return getattr(dis, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names dis offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import dis

    return sorted(item for item in dir(dis) if not item.startswith("_"))


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
pytest 864-dis
```

## 4. Open the notebook

```bash
jupyter notebook 864-dis/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `dis` | A standard library module for dis |

## Your turn

1. Open the REPL, `import dis`, then call `dir(dis)`.

## Read more

- [`dis` module docs](https://docs.python.org/3/library/dis.html)

---

[← 863-bytecode](../863-bytecode/) · [Next: 865-code-objects →](../865-code-objects/)
