# 504 · Platform

`platform` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `platform` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 504-platform/lesson_504_platform.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_504_platform.py</code></summary>

```python
"""Platform.

`platform` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 504-platform/lesson_504_platform.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import platform

    return getattr(platform, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names platform offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import platform

    return sorted(item for item in dir(platform) if not item.startswith("_"))


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
pytest 504-platform
```

## 4. Open the notebook

```bash
jupyter notebook 504-platform/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `platform` | A standard library module for platform |

## Your turn

1. Open the REPL, `import platform`, then call `dir(platform)`.

## Read more

- [`platform` module docs](https://docs.python.org/3/library/platform.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 503-sys](../503-sys/) · [Next: 505-shutil →](../505-shutil/)
