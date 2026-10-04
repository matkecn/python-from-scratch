# Roadmap

The course has 999 lessons. They are all present, runnable and tested from day
one. What changes over time is how much hand writing each one has.

## The four phases

| Phase | What happens | State |
| --- | --- | --- |
| 1. Scaffold | All 999 folders exist with the same four files, every example runs, every test passes, every notebook opens | done |
| 2. Hand write | One section at a time, replacing drafts with real lessons | in progress |
| 3. Fill the gaps | Add `exercises/` to finished lessons once the pattern is proven | planned |
| 4. Capstones | The last 49 lessons become real projects with briefs and marking schemes | planned |

## Section by section

| Lessons | Section | Level | Lessons hand written |
| --- | --- | --- | --- |
| 001-020 | Getting started | 1 | 20 of 20 done |
| 021-050 | Data types | 1 | 0 of 30 |
| 051-070 | Control flow | 2 | 0 of 20 |
| 071-100 | Collections | 2 | 0 of 30 |
| 101-120 | Strings | 2 | 0 of 20 |
| 121-160 | Functions | 2 | 0 of 40 |
| 161-200 | Modules and exceptions | 3 | 0 of 40 |
| 201-250 | Object oriented programming | 3 | 0 of 50 |
| 251-300 | Iterators and generators | 3 | 0 of 50 |
| 301-350 | Decorators and descriptors | 4 | 0 of 50 |
| 351-400 | Typing and dataclasses | 3 | 0 of 50 |
| 401-450 | The data model | 4 | 0 of 50 |
| 451-500 | Files and serialization | 2 | 0 of 50 |
| 501-580 | Standard library | 2 | 0 of 80 |
| 581-600 | CLI and logging | 3 | 0 of 20 |
| 601-650 | Networking and databases | 4 | 0 of 50 |
| 651-700 | Web and security | 4 | 0 of 50 |
| 701-740 | Testing and debugging | 3 | 0 of 40 |
| 741-800 | Packaging and CI | 3 | 0 of 60 |
| 801-840 | Concurrency and asyncio | 4 | 0 of 40 |
| 841-900 | Performance and internals | 5 | 0 of 60 |
| 901-950 | Practical Python | 4 | 0 of 50 |
| 951-999 | Projects and challenges | 5 | 0 of 49 |

Check the live count any time with:

```bash
python3 tools/scaffold.py --report
```

## Drafts are honest

A generated lesson says so in three places: the README status line, the
notebook header, and the blurb itself. A draft still has real code, real tests
and a runnable `main`, so nothing in this course is ever broken. It is simply
not finished, and it says that.

## What a finished lesson looks like

* Two or three functions, each with a summary line, `Args:`, `Returns:`,
  `Raises:` where relevant, and at least one `Examples:` block that runs as a test.
* One test per promise, named after the behaviour rather than the function.
* A `practice` list a beginner can finish in five minutes.
* Two or three glossary words, chosen because beginners trip on them.
* A `main()` that prints something you can check by eye.

## Suggested order after section one

1. 021-050 data types, because everything else leans on them.
2. 051-070 control flow, then 071-100 collections.
3. 121-160 functions, then 161-200 modules and exceptions.
4. 251-300 iteration, which unlocks the rest of the standard library.
5. 451-500 files, so later sections can read real data.
6. 701-740 testing, before the big practical sections.
