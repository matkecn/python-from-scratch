# 018 · Keywords

Keywords are the words Python keeps for itself.

**Section** Getting started and first programs · **Level** 1 of 5 · **Time** about 10 minutes · **Status** hand written

## You will learn

- There are only a few dozen keywords
- `keyword.iskeyword` checks a word
- You cannot use a keyword as a name

## 1. Run the example

```bash
python 018-keywords/lesson_018_keywords.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_018_keywords.py</code></summary>

```python
"""Keywords.

Keywords are the words Python owns. You cannot use them as names, which is a
small price for a language that reads the same everywhere.

Run me:
    python 018-keywords/lesson_018_keywords.py
"""

from __future__ import annotations

import keyword

EXAMPLES = {
    "if": "starts a condition",
    "for": "starts a loop",
    "def": "starts a function",
    "return": "sends a value back",
    "class": "starts a class",
    "True": "a value that is always on",
}


def is_keyword(word: str) -> bool:
    """Say whether a word belongs to Python.

    Args:
        word: The word to check.

    Returns:
        ``True`` when Python reserves it.

    Examples:
        >>> is_keyword("if")
        True
        >>> is_keyword("iffy")
        False
    """
    return keyword.iskeyword(word)


def explain(word: str) -> str:
    """Say what a keyword is for.

    Args:
        word: The keyword to explain.

    Returns:
        A short sentence, or a note that the word is not a keyword.

    Examples:
        >>> explain("for")
        'for starts a loop'
        >>> explain("banana")
        "'banana' is not a Python keyword"
    """
    if word in EXAMPLES:
        return f"{word} {EXAMPLES[word]}"
    if is_keyword(word):
        return f"{word} is a Python keyword"
    return f"{word!r} is not a Python keyword"


def all_keywords() -> list[str]:
    """Return every keyword Python has.

    Returns:
        A sorted list of keywords.
    """
    return sorted(keyword.kwlist)


def safe_name(word: str) -> str:
    """Return a usable version of a word.

    Args:
        word: The word you would like to use.

    Returns:
        The word with a trailing underscore when Python owns it.

    Examples:
        >>> safe_name("class")
        'class_'
        >>> safe_name("total")
        'total'
    """
    return f"{word}_" if is_keyword(word) else word


def main() -> None:
    """Look at a few keywords."""
    for word in ("if", "for", "def", "banana"):
        print(explain(word))
    print(f"{len(all_keywords())} keywords in total")


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 018-keywords
```

## 4. Open the notebook

```bash
jupyter notebook 018-keywords/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `keyword` | A word Python reserves for its own use |
| `soft keyword` | A word that is only special in certain places, such as `match` |

## Your turn

1. Print all the keywords and find the three longest.
2. Write a function that renames every keyword in a list of variable names.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/interpreter.html)

---

[← 017-statements](../017-statements/) · [Next: 019-builtins →](../019-builtins/)
