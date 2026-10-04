# 526 · Zoneinfo

`zoneinfo` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `zoneinfo` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 526-zoneinfo/lesson_526_zoneinfo.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_526_zoneinfo.py</code></summary>

```python
"""Zoneinfo.

`zoneinfo` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 526-zoneinfo/lesson_526_zoneinfo.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import zoneinfo

    return getattr(zoneinfo, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names zoneinfo offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import zoneinfo

    return sorted(item for item in dir(zoneinfo) if not item.startswith("_"))


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
pytest 526-zoneinfo
```

## 4. Open the notebook

```bash
jupyter notebook 526-zoneinfo/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `zoneinfo` | A standard library module for zoneinfo |

## Your turn

1. Open the REPL, `import zoneinfo`, then call `dir(zoneinfo)`.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 525-timezone](../525-timezone/) · [Next: 527-strftime →](../527-strftime/)
