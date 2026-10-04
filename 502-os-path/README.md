# 502 · Os-path

Placeholder for **Os-path**. A later phase replaces this with a full lesson.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 502-os-path/lesson_502_os_path.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_502_os_path.py</code></summary>

```python
"""Os-path.

Placeholder for **Os-path**. A later phase replaces this with a full lesson.

Run me:
    python 502-os-path/lesson_502_os_path.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"os path"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Os-path" for step in (1, 2, 3))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(outline())
    print(keywords())


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 502-os-path
```

## 4. Open the notebook

```bash
jupyter notebook 502-os-path/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [`os` module docs](https://docs.python.org/3/library/os.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 501-os](../501-os/) · [Next: 503-sys →](../503-sys/)
