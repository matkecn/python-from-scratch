"""Renderers that turn a :class:`~tools.lesson_model.Lesson` into files."""

from __future__ import annotations

import json
from typing import Any

from lesson_model import STATUS_DRAFT, Lesson

__all__ = [
    "LEVELS",
    "TIME_MINUTES",
    "docs_links",
    "render_readme",
    "render_notebook",
]

DOCS = "https://docs.python.org/3"

LEVELS = {
    "meta": 1,
    "getting-started": 1,
    "data-types": 1,
    "control-flow": 2,
    "collections": 2,
    "strings": 2,
    "functions": 2,
    "modules": 3,
    "oop": 3,
    "iterators": 3,
    "power-features": 4,
    "typing": 3,
    "data-model": 4,
    "files": 2,
    "stdlib": 2,
    "cli-logging": 3,
    "networking": 4,
    "web-security": 4,
    "testing": 3,
    "packaging": 3,
    "concurrency": 4,
    "internals": 5,
    "practical": 4,
    "projects": 5,
}

TIME_MINUTES = {
    1: 10,
    2: 15,
    3: 25,
    4: 40,
    5: 60,
}

MODULE_DOCS = {
    "argparse": f"{DOCS}/library/argparse.html",
    "array": f"{DOCS}/library/array.html",
    "asyncio": f"{DOCS}/library/asyncio.html",
    "ast": f"{DOCS}/library/ast.html",
    "base64": f"{DOCS}/library/base64.html",
    "bisect": f"{DOCS}/library/bisect.html",
    "calendar": f"{DOCS}/library/calendar.html",
    "cmath": f"{DOCS}/library/cmath.html",
    "codecs": f"{DOCS}/library/codecs.html",
    "collections": f"{DOCS}/library/collections.html",
    "configparser": f"{DOCS}/library/configparser.html",
    "contextlib": f"{DOCS}/library/contextlib.html",
    "copy": f"{DOCS}/library/copy.html",
    "csv": f"{DOCS}/library/csv.html",
    "dataclasses": f"{DOCS}/library/dataclasses.html",
    "datetime": f"{DOCS}/library/datetime.html",
    "decimal": f"{DOCS}/library/decimal.html",
    "difflib": f"{DOCS}/library/difflib.html",
    "dis": f"{DOCS}/library/dis.html",
    "email": f"{DOCS}/library/email.html",
    "enum": f"{DOCS}/library/enum.html",
    "fractions": f"{DOCS}/library/fractions.html",
    "ftplib": f"{DOCS}/library/ftplib.html",
    "functools": f"{DOCS}/library/functools.html",
    "gc": f"{DOCS}/library/gc.html",
    "getopt": f"{DOCS}/library/getopt.html",
    "glob": f"{DOCS}/library/glob.html",
    "gzip": f"{DOCS}/library/gzip.html",
    "hashlib": f"{DOCS}/library/hashlib.html",
    "heapq": f"{DOCS}/library/heapq.html",
    "hmac": f"{DOCS}/library/hmac.html",
    "imaplib": f"{DOCS}/library/imaplib.html",
    "inspect": f"{DOCS}/library/inspect.html",
    "io": f"{DOCS}/library/io.html",
    "itertools": f"{DOCS}/library/itertools.html",
    "json": f"{DOCS}/library/json.html",
    "linecache": f"{DOCS}/library/linecache.html",
    "logging": f"{DOCS}/library/logging.html",
    "lzma": f"{DOCS}/library/lzma.html",
    "math": f"{DOCS}/library/math.html",
    "multiprocessing": f"{DOCS}/library/multiprocessing.html",
    "numbers": f"{DOCS}/library/numbers.html",
    "operator": f"{DOCS}/library/operator.html",
    "os": f"{DOCS}/library/os.html",
    "pathlib": f"{DOCS}/library/pathlib.html",
    "pdb": f"{DOCS}/library/pdb.html",
    "pickle": f"{DOCS}/library/pickle.html",
    "platform": f"{DOCS}/library/platform.html",
    "pprint": f"{DOCS}/library/pprint.html",
    "pstats": f"{DOCS}/library/pstats.html",
    "queue": f"{DOCS}/library/queue.html",
    "random": f"{DOCS}/library/random.html",
    "re": f"{DOCS}/library/re.html",
    "secrets": f"{DOCS}/library/secrets.html",
    "shelve": f"{DOCS}/library/shelve.html",
    "shlex": f"{DOCS}/library/shlex.html",
    "shutil": f"{DOCS}/library/shutil.html",
    "signal": f"{DOCS}/library/signal.html",
    "smtplib": f"{DOCS}/library/smtplib.html",
    "socket": f"{DOCS}/library/socket.html",
    "sqlite3": f"{DOCS}/library/sqlite3.html",
    "ssl": f"{DOCS}/library/ssl.html",
    "stat": f"{DOCS}/library/stat.html",
    "statistics": f"{DOCS}/library/statistics.html",
    "struct": f"{DOCS}/library/struct.html",
    "subprocess": f"{DOCS}/library/subprocess.html",
    "sys": f"{DOCS}/library/sys.html",
    "tarfile": f"{DOCS}/library/tarfile.html",
    "tempfile": f"{DOCS}/library/tempfile.html",
    "textwrap": f"{DOCS}/library/textwrap.html",
    "threading": f"{DOCS}/library/threading.html",
    "timeit": f"{DOCS}/library/timeit.html",
    "tomllib": f"{DOCS}/library/tomllib.html",
    "traceback": f"{DOCS}/library/traceback.html",
    "tracemalloc": f"{DOCS}/library/tracemalloc.html",
    "types": f"{DOCS}/library/types.html",
    "typing": f"{DOCS}/library/typing.html",
    "unicodedata": f"{DOCS}/library/unicodedata.html",
    "unittest": f"{DOCS}/library/unittest.html",
    "urllib": f"{DOCS}/library/urllib.html",
    "uuid": f"{DOCS}/library/uuid.html",
    "warnings": f"{DOCS}/library/warnings.html",
    "weakref": f"{DOCS}/library/weakref.html",
    "xml": f"{DOCS}/library/xml.html",
    "zipfile": f"{DOCS}/library/zipfile.html",
    "zlib": f"{DOCS}/library/zlib.html",
}

TUTORIAL_PAGES = {
    "getting-started": "interpreter.html",
    "data-types": "introduction.html",
    "control-flow": "controlflow.html",
    "collections": "datastructures.html",
    "strings": "strings.html",
    "functions": "functions.html",
    "modules": "modules.html",
    "oop": "classes.html",
    "iterators": "classes.html",
    "power-features": "classes.html",
    "typing": "typing.html",
    "data-model": "datamodel.html",
    "files": "inputoutput.html",
    "stdlib": "modules.html",
    "testing": "unittest.html",
    "errors": "errors.html",
}


def level_for(section: str) -> int:
    """Return the 1 to 5 difficulty number for a section key."""
    return LEVELS.get(section, 3)


def docs_links(section: str, slug: str, extra: tuple[str, ...]) -> list[str]:
    """Return documentation links for a lesson, most specific first."""
    links: list[str] = []
    for word in slug.replace("_", "-").split("-"):
        if word in MODULE_DOCS:
            links.append(f"[`{word}` module docs]({MODULE_DOCS[word]})")
    page = TUTORIAL_PAGES.get(section)
    if page:
        links.append(f"[official tutorial]({DOCS}/tutorial/{page})")
    links.extend(extra)
    if not links:
        links.append(f"[language reference]({DOCS}/reference/index.html)")
        links.append(f"[glossary]({DOCS}/glossary.html)")
    seen: list[str] = []
    for link in links:
        if link not in seen:
            seen.append(link)
    return seen


def render_readme(topic: Any, lesson: Lesson, section_title: str, prev_link: str, next_link: str) -> str:
    """Return the README markdown for one lesson."""
    level = level_for(topic.section)
    badge = "hand written" if lesson.status != STATUS_DRAFT else "generated draft (Phase 2)"
    parts: list[str] = [
        f"# {topic.number:03d} · {topic.title}",
        "",
        lesson.blurb,
        "",
        f"**Section** {section_title} · **Level** {level} of 5 · "
        f"**Time** about {TIME_MINUTES[level]} minutes · **Status** {badge}",
        "",
        "## You will learn",
        "",
    ]
    parts += [f"- {point}" for point in lesson.points]
    parts += [
        "",
        "## 1. Run the example",
        "",
        "```bash",
        f"python {topic.folder}/{topic.module}.py",
        "```",
        "",
        "## 2. Read the code",
        "",
        "<details>",
        "<summary>Show <code>" + topic.module + ".py</code></summary>",
        "",
        "```python",
        lesson.source.rstrip(),
        "```",
        "",
        "</details>",
        "",
        "## 3. Run the tests",
        "",
        "```bash",
        f"pytest {topic.folder}",
        "```",
        "",
        "## 4. Open the notebook",
        "",
        "```bash",
        f"jupyter notebook {topic.folder}/lesson.ipynb",
        "```",
    ]
    if lesson.glossary:
        parts += ["", "## Words to remember", "", "| word | meaning |", "| --- | --- |"]
        parts += [f"| `{word}` | {meaning} |" for word, meaning in lesson.glossary]
    if lesson.practice:
        parts += ["", "## Your turn", ""]
        parts += [f"{index}. {task}" for index, task in enumerate(lesson.practice, start=1)]
    parts += ["", "## Read more", ""]
    parts += [f"- {link}" for link in docs_links(topic.section, topic.slug, lesson.read_more)]
    if next_link:
        footer = f"[← {prev_link}](../{prev_link}/) · [Next: {next_link} →](../{next_link}/)"
    else:
        footer = f"[← {prev_link}](../{prev_link}/) · [Back to the course index](../../README.md)"
    parts += [
        "",
        "---",
        "",
        footer,
        "",
    ]
    return "\n".join(parts)


def _md(source: str) -> dict[str, Any]:
    return {"cell_type": "markdown", "metadata": {}, "source": source}


def _code(source: str) -> dict[str, Any]:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source,
    }


def render_notebook(topic: Any, lesson: Lesson, prev_link: str, next_link: str) -> str:
    """Return the ``.ipynb`` json text for one lesson."""
    level = level_for(topic.section)
    intro = "\n".join(
        [
            f"# {topic.number:03d} · {topic.title}",
            "",
            lesson.blurb,
            "",
            f"**Section** {topic.section} · **Level** {level} of 5",
            "",
            "## You will learn",
            "",
            *(f"- {point}" for point in lesson.points),
        ]
    )
    cells: list[dict[str, Any]] = [_md(intro)]
    cells.append(
        _md(
            "\n".join(
                [
                    "## 1. Run the finished example",
                    "",
                    "This runs the file in this folder and shows its output.",
                ]
            )
        )
    )
    cells.append(_code(f"!python {topic.module}.py\n"))
    names = lesson.names()
    if names:
        listed = ", ".join(f"`{name}`" for name in names)
        cells.append(_md(f"## 2. Play with the functions\n\nThis lesson gives you: {listed}\n"))
        cells.append(
            _code(
                f"from {topic.module} import {', '.join(names)}\n\n"
                f"print({names[0]}({'1' if names[0] != 'main' else ''}))\n"
            )
        )
    cells.append(
        _md(
            "\n".join(
                [
                    "## 3. Read the code",
                    "",
                    "<details><summary>Show the whole example</summary>",
                    "",
                    "```python",
                    lesson.source.rstrip(),
                    "```",
                    "",
                    "</details>",
                ]
            )
        )
    )
    if lesson.practice:
        cells.append(_md("## 4. Your turn\n\nChange the code until the tests fail, then make them pass."))
        for task in lesson.practice:
            cells.append(_md(f"**Task** {task}\n"))
            cells.append(_code("# Write your answer here.\n"))
    else:
        cells.append(_md("## 4. Your turn\n\nOpen `lesson.ipynb`, change a number, run it again, and watch what changes."))
        cells.append(_code("# Write your answer here.\n"))
    if next_link:
        footer = f"[← {prev_link}](../{prev_link}/) · [Next: {next_link} →](../{next_link}/)"
    else:
        footer = f"[← {prev_link}](../{prev_link}/) · [You finished the course](../../README.md)"
    cells.append(
        _md(
            "\n".join(
                [
                    "## 5. Check yourself",
                    "",
                    "```bash",
                    f"pytest {topic.folder}",
                    "```",
                    "",
                    "---",
                    "",
                    footer,
                ]
            )
        )
    )
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.12"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    return json.dumps(notebook, indent=1, ensure_ascii=False) + "\n"
