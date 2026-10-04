# 470 · File-copy

Files let your code remember things after it stops.

**Section** Files, paths and serialization · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- `open` a file to read or write
- `with` closes it for you
- Use `pathlib` for paths

## 1. Run the example

```bash
python 470-file-copy/lesson_470_file_copy.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_470_file_copy.py</code></summary>

```python
"""File-copy.

Files let your code remember things after it stops.

Run me:
    python 470-file-copy/lesson_470_file_copy.py
"""

from __future__ import annotations


from pathlib import Path


def save_lines(lines: list[str], path: str) -> int:
    """Write lines to a file and return how many were written.

    Args:
        lines: The lines to save.
        path: Where to save them.

    Returns:
        The number of lines written.
    """
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines))
    return len(lines)


def read_lines(path: str) -> list[str]:
    """Read lines back from a file.

    Args:
        path: The file to read.

    Returns:
        The lines that were in the file.
    """
    return Path(path).read_text(encoding="utf-8").splitlines()


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    import tempfile

    folder = tempfile.mkdtemp()
    target = f"{folder}/demo.txt"
    print(save_lines(["one", "two"], target))
    print(read_lines(target))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 470-file-copy
```

## 4. Open the notebook

```bash
jupyter notebook 470-file-copy/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `file` | Text or data saved on disk |
| `context manager` | The object behind `with`, which tidies up for you |

## Read more

- [`copy` module docs](https://docs.python.org/3/library/copy.html)
- [official tutorial](https://docs.python.org/3/tutorial/inputoutput.html)

---

[← 469-directory-operations](../469-directory-operations/) · [Next: 471-file-move →](../471-file-move/)
