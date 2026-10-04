# 715 · Set-up-tear-down

A set keeps unique values with no duplicates.

**Section** Debugging and testing · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Sets have no order
- Duplicates disappear
- `|` joins two sets

## 1. Run the example

```bash
python 715-set-up-tear-down/lesson_715_set_up_tear_down.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_715_set_up_tear_down.py</code></summary>

```python
"""Set-up-tear-down.

A set keeps unique values with no duplicates.

Run me:
    python 715-set-up-tear-down/lesson_715_set_up_tear_down.py
"""

from __future__ import annotations


def unique_letters(text: str) -> set[str]:
    """Return every different letter in the text.

    Args:
        text: The text to look at.

    Returns:
        A set of letters.

    Examples:
        >>> sorted(unique_letters("aab"))
        ['a', 'b']
    """
    return set(text)


def shared(first: set[str], second: set[str]) -> set[str]:
    """Return the letters that appear in both sets.

    Args:
        first: The first set.
        second: The second set.

    Returns:
        The letters found in both.
    """
    return first & second


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(sorted(unique_letters("banana")))
    print(sorted(shared({"a", "b"}, {"b", "c"})))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 715-set-up-tear-down
```

## 4. Open the notebook

```bash
jupyter notebook 715-set-up-tear-down/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `set` | A box of unique things with no order |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/unittest.html)

---

[← 714-assertions](../714-assertions/) · [Next: 716-test-fixtures →](../716-test-fixtures/)
