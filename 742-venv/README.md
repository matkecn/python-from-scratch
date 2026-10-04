# 742 · Venv

`venv` is a standard library module. This lesson shows how to look inside one.

**Section** Packaging, style, CI and documentation · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `venv` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 742-venv/lesson_742_venv.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_742_venv.py</code></summary>

```python
"""Venv.

`venv` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 742-venv/lesson_742_venv.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import venv

    return getattr(venv, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names venv offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import venv

    return sorted(item for item in dir(venv) if not item.startswith("_"))


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
pytest 742-venv
```

## 4. Open the notebook

```bash
jupyter notebook 742-venv/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `venv` | A standard library module for venv |

## Your turn

1. Open the REPL, `import venv`, then call `dir(venv)`.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 741-virtual-environments](../741-virtual-environments/) · [Next: 743-pip →](../743-pip/)
