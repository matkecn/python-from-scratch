# Contributing

Thank you for helping. This page is short on purpose.

## The rules

1. **One idea per lesson.** If the title needs an "and", it is two lessons.
2. **Two or three functions.** Enough to teach the idea, few enough to read in
   one sitting.
3. **A docstring on the module and on every public function or class.** A
   summary line, then `Args:`, `Returns:` and `Raises:` where they apply.
4. **At least one `Examples:` block** in every docstring. These run as tests, so
   a wrong example fails the build.
5. **One test per promise.** Name the test after the behaviour, not the
   function: `test_swapping_twice_is_safe`, not `test_swap2`.
6. **A runnable `main()`.** `python lesson_013_variables.py` must always print
   something you can check by eye.
7. **Short code.** If an example passes thirty lines, it is two lessons.
8. **No wall of text.** Three to five bullets for "You will learn".

## Writing a lesson

Hand written lessons live in `tools/written/`, in files named after their
section, for example `s001_intro.py`. Each one is a dictionary keyed by lesson
number:

```python
LESSONS: dict[int, Lesson] = {
    13: lesson(
        blurb="A variable is a name that remembers a value.",
        points=("Store a value with `=`", "Swap two values in one line"),
        source='''"""Variables.

Run me:
    python 013-variables/lesson_013_variables.py
"""
...
''',
        tests='''"""Tests for Variables."""
...
''',
        practice=("Make three variables and print a story about them.",),
        glossary=(("variable", "A name that points at a value"),),
    ),
}
```

Then write the files:

```bash
python3 tools/scaffold.py --only 13 --force 13
```

That rewrites all four files for lesson 13 from your text. The README and the
notebook are generated from the same data, so they can never disagree with the
code.

## Before you open a pull request

```bash
pytest                        # every test and every docstring example
python3 tools/verify.py       # every lesson complete, runnable, valid notebook
ruff check .                  # style, if you have ruff installed
```

All three must be clean.

## Style

* Follow the code in `001-getting-started` to `020-first-program`. Match it
  rather than inventing a new style.
* Four spaces per indent. One blank line between functions. Two between top
  level blocks.
* Type hints on every function signature, even the simple ones.
* Docstrings in the Google style already used throughout: summary, `Args:`,
  `Returns:`, `Raises:`, `Examples:`.
* Say why in a comment, never what.

## Adding a topic

`structure.a` is the source of truth for the 999 topics. To add one:

1. Add the line to `structure.a` in the right section.
2. Run `python3 tools/build_curriculum.py`.
3. Write the lesson in `tools/written/`.
4. Run `python3 tools/scaffold.py --only <number> --force <number>`.
5. Run `pytest <folder>`.

The integrity test in [`test_course_integrity.py`](test_course_integrity.py)
will tell you if numbering, folders or links are wrong.

## Reporting a problem

Open an issue with the lesson number, for example `041-arithmetic`, what you
expected, and what happened instead. A failing example is the most useful bug
report there is.
