# 970 · Dictionary-challenges

A dictionary stores values under keys, like a phone book.

**Section** Projects, challenges and mastery · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- Make a dictionary with `{ }`
- Look a value up by its key
- `get` gives a safe default

## 1. Run the example

```bash
python 970-dictionary-challenges/lesson_970_dictionary_challenges.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_970_dictionary_challenges.py</code></summary>

```python
"""Dictionary-challenges.

A dictionary stores values under keys, like a phone book.

Run me:
    python 970-dictionary-challenges/lesson_970_dictionary_challenges.py
"""

from __future__ import annotations


def word_lengths(text: str) -> dict[str, int]:
    """Map each word to the number of letters it has.

    Args:
        text: A sentence.

    Returns:
        A dictionary of word to length.

    Examples:
        >>> word_lengths("a bb")
        {'a': 1, 'bb': 2}
    """
    return {word: len(word) for word in text.split()}


def lookup(ages: dict[str, int], name: str) -> int:
    """Return someone's age, or ``-1`` when we do not know them.

    Args:
        ages: A mapping of name to age.
        name: The person to look up.

    Returns:
        The age, or ``-1``.

    Examples:
        >>> lookup({"Ada": 36}, "Bo")
        -1
    """
    return ages.get(name, -1)


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(word_lengths("a bb ccc"))
    print(lookup({"Ada": 36}, "Bo"))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 970-dictionary-challenges
```

## 4. Open the notebook

```bash
jupyter notebook 970-dictionary-challenges/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `key` | The name you look up |
| `value` | The thing you find |

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 969-list-challenges](../969-list-challenges/) · [Next: 971-recursion-challenges →](../971-recursion-challenges/)
