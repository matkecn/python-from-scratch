# 506 · Subprocess

`subprocess` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `subprocess` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 506-subprocess/lesson_506_subprocess.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_506_subprocess.py</code></summary>

```python
"""Subprocess.

`subprocess` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 506-subprocess/lesson_506_subprocess.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import subprocess

    return getattr(subprocess, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names subprocess offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import subprocess

    return sorted(item for item in dir(subprocess) if not item.startswith("_"))


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
pytest 506-subprocess
```

## 4. Open the notebook

```bash
jupyter notebook 506-subprocess/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `subprocess` | A standard library module for subprocess |

## Your turn

1. Open the REPL, `import subprocess`, then call `dir(subprocess)`.

## Read more

- [`subprocess` module docs](https://docs.python.org/3/library/subprocess.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 505-shutil](../505-shutil/) · [Next: 507-environment-variables →](../507-environment-variables/)
