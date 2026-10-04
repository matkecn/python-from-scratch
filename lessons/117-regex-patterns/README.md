# 117 · Regex-patterns

Regular expressions find patterns inside text.

**Section** Strings, encodings and regular expressions · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- `re.search` finds the first match
- Raw strings keep backslashes readable
- Groups capture pieces

## 1. Run the example

```bash
python 117-regex-patterns/lesson_117_regex_patterns.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_117_regex_patterns.py</code></summary>

```python
"""Regex-patterns.

Regular expressions find patterns inside text.

Run me:
    python 117-regex-patterns/lesson_117_regex_patterns.py
"""

from __future__ import annotations


import re


def find_digits(text: str) -> list[str]:
    """Return every run of digits in the text.

    Args:
        text: The text to search.

    Returns:
        The digit groups, in order.

    Examples:
        >>> find_digits("a1 b22")
        ['1', '22']
    """
    return re.findall(r"\d+", text)


def is_valid_pin(pin: str) -> bool:
    """Say whether a pin is exactly four digits.

    Args:
        pin: The pin to check.

    Returns:
        ``True`` when the pin is four digits.

    Examples:
        >>> is_valid_pin("1234")
        True
    """
    return bool(re.fullmatch(r"\d{4}", pin))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(find_digits("a1 b22"))
    print(is_valid_pin("1234"), is_valid_pin("12"))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 117-regex-patterns
```

## 4. Open the notebook

```bash
jupyter notebook 117-regex-patterns/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `regex` | A small language for finding text patterns |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/strings.html)

---

[← 116-regex-introduction](../116-regex-introduction/) · [Next: 118-regex-groups →](../118-regex-groups/)
