# 000 · Meta

This folder is about the course itself: where it is going, how to help, and the
rules every lesson follows.

| File | What it is for |
| --- | --- |
| [`ROADMAP.md`](ROADMAP.md) | Which sections are finished and which are still drafts |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to write or improve a lesson |
| [`LICENSE`](LICENSE) | MIT, so you can use and reuse everything here |
| [`test_course_integrity.py`](test_course_integrity.py) | A test that checks the course itself |

## The rules every lesson follows

1. **One idea per lesson.** If the folder name needs an "and", it is two lessons.
2. **Two or three functions.** Enough to show the idea, few enough to read.
3. **A docstring on everything.** A summary line, then `Args:`, `Returns:` and
   `Raises:` where they apply, plus at least one `Examples:` block.
4. **One test per promise.** If the docstring says it, a test checks it.
5. **A runnable `main()`.** `python lesson_013_variables.py` must always do
   something visible.
6. **No long code.** If an example passes thirty lines, it is two lessons.

## How the files are made

`structure.a` lists all 999 topics in order and is the source of truth.

```text
structure.a  ->  tools/build_curriculum.py  ->  tools/curriculum.py
tools/written/  ---------------------------->  hand written lessons win
tools/synth.py  --------------------------->  generated drafts for the rest
tools/scaffold.py  ------------------------->  README.md, example, tests, notebook
```

Run the whole chain again with:

```bash
python3 tools/build_curriculum.py
python3 tools/scaffold.py --report
python3 tools/scaffold.py
python3 tools/verify.py
```

## The integrity test

`test_course_integrity.py` checks the promises this page makes. Run it with:

```bash
pytest 000-meta
```

It confirms that there are 999 numbered lessons, that every folder name and
module name is unique, that every lesson has all four files, and that the
previous and next links in every README actually point somewhere.
