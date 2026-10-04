<a id="top"></a>

<div align="center">

# 🐍 python-from-scratch

### A 999-lesson Python course where every lesson is runnable, tested and notebook-ready

[![Python](https://img.shields.io/badge/python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Lessons](https://img.shields.io/badge/lessons-999-00C853)](000-meta/ROADMAP.md)
[![Tests](https://img.shields.io/badge/tests-2289%20passing-4C1)](000-meta/README.md)
[![Notebooks](https://img.shields.io/badge/notebooks-1000-FF69B4)](000-welcome/lesson.ipynb)
[![Sections](https://img.shields.io/badge/sections-24-8957E5)](000-meta/ROADMAP.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-2EA44F)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/matkecn/python-from-scratch?label=%20last%20commit)](https://github.com/matkecn/python-from-scratch/commits/main)
[![Stars](https://img.shields.io/github/stars/matkecn/python-from-scratch?label=%20%F0%9F%8C%99%20stars&style=social)](https://github.com/matkecn/python-from-scratch/stargazers)
[![Forks](https://img.shields.io/github/forks/matkecn/python-from-scratch?label=%20%F0%9F%93%B4%20forks&style=social)](https://github.com/matkecn/python-from-scratch/network/members)
[![Issues](https://img.shields.io/github/issues/matkecn/python-from-scratch?label=%20%F0%9F%94%A5%20issues)](https://github.com/matkecn/python-from-scratch/issues)

</div>

---

## 📑 Table of Contents

| # | Section | What you find |
| --- | --- | --- |
| 1 | [🚀 Quick Start](#quick-start) | Get running in four commands |
| 2 | [📖 How a Lesson Works](#how-a-lesson-works) | The four files in every folder |
| 3 | [🗺️ The Course Map](#the-course-map) | All 24 sections, in order |
| 4 | [✨ Why It Is Built This Way](#why-it-is-built-this-way) | The rules every lesson follows |
| 5 | [✅ Quality Gates](#quality-gates) | How every lesson is checked |
| 6 | [🧰 Project Layout](#project-layout) | The repository at a glance |
| 7 | [🛠️ Tooling](#tooling) | Generator, scaffolder, verifier |
| 8 | [🤝 Contributing](#contributing) | Write or improve a lesson |
| 9 | [🗺️ Roadmap](#roadmap) | What is finished, what is next |
| 10 | [📄 License](#license) | MIT |

---

<a id="quick-start"></a>

## 🚀 Quick Start

You need **Python 3.11 or newer**. Nothing else is required to read the
lessons; the extras below are for running the tests and the notebooks.

```bash
# 1. clone the course
git clone https://github.com/matkecn/python-from-scratch.git
cd python-from-scratch

# 2. create a virtual environment (optional, but tidy)
python3 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. install the tools used by the tests and notebooks
python3 -m pip install -r requirements-dev.txt

# 4. run one lesson
python 013-variables/lesson_013_variables.py
```

Prefer clicking? Open any notebook straight from the site, or locally:

```bash
jupyter notebook 013-variables/lesson.ipynb
```

New here? Read these three folders in order:

| Order | Folder | What it does |
| --- | --- | --- |
| 1️⃣ | [`000-welcome`](000-welcome/README.md) | Your first program, one line of Python |
| 2️⃣ | [`001-getting-started`](001-getting-started/README.md) | Install Python and learn to run a file |
| 3️⃣ | [`020-first-program`](020-first-program/README.md) | A small quiz program that actually works |

---

<a id="how-a-lesson-works"></a>

## 📖 How a Lesson Works

Every one of the 999 lessons is one folder with the same four files, so you
always know where to look:

```text
013-variables/
├── README.md                       📖 the lesson, written to be read
├── lesson_013_variables.py         🐍 tiny runnable example
├── test_lesson_013_variables.py    🧪 tests that prove it works
└── lesson.ipynb                   📓 the same lesson as a notebook
```

A lesson always asks the same four things:

```bash
# 1️⃣ run it and see what it prints
python 013-variables/lesson_013_variables.py

# 2️⃣ read the code (it is also inside the README)
cat 013-variables/lesson_013_variables.py

# 3️⃣ run the tests
pytest 013-variables

# 4️⃣ open the notebook and try the exercises
jupyter notebook 013-variables/lesson.ipynb
```

### 🐍 What the code looks like

Short, typed, and documented. Every function says what it expects, what it
returns and what can go wrong, with examples that run as tests:

```python
def make_greeting(name: str) -> str:
    """Build a greeting for someone.

    Args:
        name: The person's name.

    Returns:
        A greeting ending with an exclamation mark.

    Examples:
        >>> make_greeting("Ada")
        'Hello, Ada!'
    """
    return f"Hello, {name}!"
```

### 📓 What the notebook gives you

| Cell | What it does |
| --- | --- |
| 1 | The lesson summary and what you will learn |
| 2 | Runs the finished example with `!python` |
| 3 | Imports the functions so you can call them |
| 4 | The full source, plus a **Your turn** cell |
| 5 | The command to check your own work, plus links to the neighbours |

---

<a id="the-course-map"></a>

## 🗺️ The Course Map

999 lessons, 24 sections, ordered so that nothing appears before you need it.

| # | Lessons | Section | Level | Start here |
| --- | --- | --- | :-: | --- |
| 1 | 001–020 | 🟢 Getting started and first programs | 1 | [`001-getting-started`](001-getting-started/README.md) |
| 2 | 021–050 | 🟢 Data types and conversions | 1 | [`021-integers`](021-integers/README.md) |
| 3 | 051–070 | 🟢 Conditionals and loops | 2 | [`051-if`](051-if/README.md) |
| 4 | 071–100 | 🟢 Lists, tuples, sets and dictionaries | 2 | [`071-lists`](071-lists/README.md) |
| 5 | 101–120 | 🟡 Strings, encodings and regular expressions | 2 | [`101-string-indexing`](101-string-indexing/README.md) |
| 6 | 121–160 | 🟡 Functions, arguments and scope | 2 | [`121-functions`](121-functions/README.md) |
| 7 | 161–200 | 🟡 Modules, imports and exceptions | 3 | [`161-modules`](161-modules/README.md) |
| 8 | 201–250 | 🟠 Object oriented programming | 3 | [`201-classes`](201-classes/README.md) |
| 9 | 251–300 | 🟠 Iterators, generators and collections | 3 | [`251-iterables`](251-iterables/README.md) |
| 10 | 301–350 | 🟠 Decorators, context managers, descriptors | 4 | [`301-decorators`](301-decorators/README.md) |
| 11 | 351–400 | 🟡 Type hints, dataclasses, pattern matching | 3 | [`351-type-hints`](351-type-hints/README.md) |
| 12 | 401–450 | 🔴 The Python data model, dunder by dunder | 4 | [`401-dunder-methods`](401-dunder-methods/README.md) |
| 13 | 451–500 | 🟢 Files, paths and serialization | 2 | [`451-files`](451-files/README.md) |
| 14 | 501–580 | 🟢 Standard library tour | 2 | [`501-os`](501-os/README.md) |
| 15 | 581–600 | 🟡 Command line tools and logging | 3 | [`581-argparse`](581-argparse/README.md) |
| 16 | 601–650 | 🔴 Networking, APIs and databases | 4 | [`601-sockets`](601-sockets/README.md) |
| 17 | 651–700 | 🔴 Web concepts, scraping and security | 4 | [`651-web-concepts`](651-web-concepts/README.md) |
| 18 | 701–740 | 🟡 Debugging and testing | 3 | [`701-debugging`](701-debugging/README.md) |
| 19 | 741–800 | 🟡 Packaging, style, CI and documentation | 3 | [`741-virtual-environments`](741-virtual-environments/README.md) |
| 20 | 801–840 | 🔴 Concurrency and asyncio | 4 | [`801-concurrency`](801-concurrency/README.md) |
| 21 | 841–900 | 🔴 Performance, memory and CPython internals | 5 | [`841-performance`](841-performance/README.md) |
| 22 | 901–950 | 🔴 Practical Python applications | 4 | [`901-cli-apps`](901-cli-apps/README.md) |
| 23 | 951–999 | 🔴 Projects, challenges and mastery | 5 | [`951-beginner-project-01`](951-beginner-project-01/README.md) |

🟢 beginner · 🟡 early intermediate · 🟠 intermediate · 🔴 advanced

The full topic list lives in [`structure.a`](structure.a) and the progress of
each section lives in [`000-meta/ROADMAP.md`](000-meta/ROADMAP.md).

---

<a id="why-it-is-built-this-way"></a>

## ✨ Why It Is Built This Way

| | |
| --- | --- |
| 🐾 **Toddler sized** | Two or three tiny functions per lesson. Nothing is longer than a screen, so the whole idea fits in your head. |
| 📝 **Real docstrings** | Every function has a summary line, `Args:`, `Returns:`, `Raises:` where relevant, and at least one runnable `Examples:` block. |
| 🧪 **Tests everywhere** | Each lesson ships with tests, and every docstring example runs as a test too. If a lesson breaks, the suite says so. |
| 📓 **Notebook included** | Every lesson also exists as `lesson.ipynb` if you would rather click Run than type commands. |
| 🧭 **No surprises** | One folder per topic, numbered, in teaching order. `structure.a` is the original plan and nothing was renumbered. |
| 🏷️ **Honest status** | Generated lessons are labelled *draft* in the README and the notebook. Nothing pretends to be finished. |

---

<a id="quality-gates"></a>

## ✅ Quality Gates

```bash
pytest                      # 2075 unit tests + 214 docstring examples
python3 tools/verify.py     # runs all 999 examples, validates all 999 notebooks
python3 tools/scaffold.py --report
ruff check .                # style, when ruff is installed
```

`tools/verify.py` is the strict one. For every lesson it checks that:

- ✅ the example module compiles **and runs** as a script;
- ✅ the module, every function and every class has a docstring;
- ✅ the notebook is valid `nbformat` 4 JSON with code cells, and mentions its module;
- ✅ the test module has a docstring and at least one test;
- ✅ all four files are present.

There is also a test for the course itself,
[`000-meta/test_course_integrity.py`](000-meta/test_course_integrity.py), which
confirms there are exactly 999 numbered lessons, that folder and module names
are unique, that no lesson module shadows the standard library, and that the
previous and next links in every README point at folders that exist.

---

<a id="project-layout"></a>

## 🧰 Project Layout

```text
python-from-scratch/
├── 📄 README.md               this file
├── 📋 structure.a             the original 999 topic plan, source of truth
├── ⚙️  pyproject.toml         pytest and ruff configuration
├── 🧪 Makefile                test, verify, scaffold, lint
├── 📦 requirements-dev.txt   pytest, jupyterlab, ruff
├── 🚀 000-welcome/            your first program
├── 🧭 000-meta/               roadmap, contributing guide, licence, integrity test
├── 📚 001-getting-started/ … 999 lesson folders …
│   └── 999-final-python-capstone/
└── 🛠️  tools/                  the machinery that builds the course
    ├── build_curriculum.py    structure.a → curriculum.py
    ├── curriculum.py          generated course data
    ├── lesson_model.py        the Lesson data model
    ├── templates.py           README and notebook renderers
    ├── synth.py               generates runnable drafts
    ├── written/               hand written lessons, always win
    ├── scaffold.py            writes the four files per lesson
    ├── notebook.py            rebuilds a notebook from its example
    └── verify.py              checks every lesson
```

**Why are the modules called `lesson_013_variables.py`?** About 25 topic names
are also standard library names (`copy`, `operator`, `glob`, `json`…). A
prefixed module name keeps `import copy` meaning the real `copy`, and keeps
999 lessons from colliding with each other when pytest imports them.

---

<a id="tooling"></a>

## 🛠️ Tooling

| Command | What it does |
| --- | --- |
| `make help` | List every shortcut |
| `make test` | Run all 2289 tests |
| `make lesson SLICE=101-120` | Run the tests for one slice of the course |
| `make verify` | Check that all 999 lessons are healthy |
| `make report` | Show how many lessons are hand written and how many are drafts |
| `python3 tools/scaffold.py --only 13 --force 13` | Rewrite one lesson |
| `python3 tools/notebook.py 013-variables` | Rebuild one notebook from its code |

---

<a id="contributing"></a>

## 🤝 Contributing

New lessons, fixes and extra exercises are all welcome. The short version:

1. **One idea per lesson.** If the title needs an "and", it is two lessons.
2. **Two or three functions**, with a full docstring and an `Examples:` block.
3. **One test per promise**, named after the behaviour.
4. **A runnable `main()`** that prints something you can check by eye.
5. **Short code.** If an example passes thirty lines, it is two lessons.

Full instructions, including how to add a topic to `structure.a`, are in
[`000-meta/CONTRIBUTING.md`](000-meta/CONTRIBUTING.md). In short:

```bash
# 1. add your topic to structure.a, then
python3 tools/build_curriculum.py

# 2. write the lesson in tools/written/
# 3. generate its four files
python3 tools/scaffold.py --only 13 --force 13

# 4. prove it works
pytest 013-variables && python3 tools/verify.py --only 13
```

---

<a id="roadmap"></a>

## 🗺️ Roadmap

| Phase | What happens | State |
| --- | --- | --- |
| 1️⃣ Scaffold | All 999 folders exist, every example runs, every test passes, every notebook opens | ✅ done |
| 2️⃣ Hand write | One section at a time, replacing drafts with real lessons | 🔄 20 of 999 |
| 3️⃣ Exercises | Add an `exercises/` folder to finished lessons | ⏳ planned |
| 4️⃣ Capstones | The last 49 lessons become real projects with briefs and marking schemes | ⏳ planned |

See [`000-meta/ROADMAP.md`](000-meta/ROADMAP.md) for the section by section
table, and run `python3 tools/scaffold.py --report` for the live count.

---

<a id="license"></a>

## 📄 License

Released under the [MIT License](LICENSE). Use it, learn from it, teach with
it, fork it. A copy also lives at
[`000-meta/LICENSE`](000-meta/LICENSE).

---

<div align="center">

**Made with 🐍 and ☕ for everyone who ever wondered what `//` really means.**

[⬆ Back to top](#top)

</div>
