"""Turn ``structure.a`` into ``tools/curriculum.py``.

Run it once after editing ``structure.a``::

    python tools/build_curriculum.py

``structure.a`` stays the single source of truth. This script only reads it
and writes the machine friendly ``curriculum.py`` next to it.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "structure.a"
TARGET = Path(__file__).resolve().parent / "curriculum.py"

TREE_LINE = re.compile(r"^[\u2502\u251c\u2514]\u2500\u2500\s+(\d{3})-([a-z0-9_-]+)/\s*$")
FLAT_LINE = re.compile(r"^(\d{3})-([a-z0-9_-]+)/?\s*$")

SECTIONS: list[tuple[int, int, str, str]] = [
    (0, 0, "meta", "Meta: how to use this course"),
    (1, 20, "getting-started", "Getting started and first programs"),
    (21, 50, "data-types", "Data types and conversions"),
    (51, 70, "control-flow", "Conditionals and loops"),
    (71, 100, "collections", "Lists, tuples, sets and dictionaries"),
    (101, 120, "strings", "Strings, encodings and regular expressions"),
    (121, 160, "functions", "Functions, arguments and scope"),
    (161, 200, "modules", "Modules, imports and exceptions"),
    (201, 250, "oop", "Object oriented programming"),
    (251, 300, "iterators", "Iterators, generators and the collections library"),
    (301, 350, "power-features", "Decorators, context managers, descriptors and introspection"),
    (351, 400, "typing", "Type hints, dataclasses and pattern matching"),
    (401, 450, "data-model", "The Python data model (dunder methods)"),
    (451, 500, "files", "Files, paths and serialization"),
    (501, 580, "stdlib", "Standard library tour"),
    (581, 600, "cli-logging", "Command line tools and logging"),
    (601, 650, "networking", "Networking, APIs and databases"),
    (651, 700, "web-security", "Web concepts, scraping and security"),
    (701, 740, "testing", "Debugging and testing"),
    (741, 800, "packaging", "Packaging, style, CI and documentation"),
    (801, 840, "concurrency", "Concurrency and asyncio"),
    (841, 900, "internals", "Performance, memory and CPython internals"),
    (901, 950, "practical", "Practical Python applications"),
    (951, 999, "projects", "Projects, challenges and mastery"),
]

TITLE_FIXES = {
    "152-lebs": "Scope labs",
    "184-else-exceptions": "try, else, finally",
    "203-__init__": "__init__",
    "041-arithmetic": "Arithmetic operators",
    "045-assignment-operators": "Assignment operators",
    "082-tuple-indexing": "Tuple indexing",
    "099-ordered-dictionaries": "Ordered dictionaries",
    "112-utf8": "UTF-8",
    "113-utf16": "UTF-16",
    "114-utf32": "UTF-32",
    "133-docstrings": "Docstrings",
    "163-from-import": "from ... import",
    "164-import-as": "import ... as",
    "168-init-py": "__init__.py",
    "189-exception-chaining": "Exception chaining",
    "212-getters-setters": "Getters and setters",
    "236-new": "__new__",
    "237-init": "__init__",
    "238-del": "__del__",
    "306-preserving-metadata": "Preserving metadata",
    "345-dynamic-programming": "Dynamic programming",
    "381-dataclasses": "Dataclasses",
    "390-dataclass-patterns": "Dataclass patterns",
    "391-pattern-matching": "Pattern matching",
    "405-bytes": "__bytes__",
    "422-pow": "__pow__",
    "423-matmul": "__matmul__",
    "519-matrix-basics": "Matrix basics",
    "581-argparse": "argparse",
    "621-sql": "SQL",
    "623-sqlite-connect": "sqlite3.connect",
    "699-monitoring-basics": "Monitoring basics",
    "727-test-coverage": "Test coverage",
    "753-package-metadata": "Package metadata",
    "822-event-loop": "Event loop",
    "858-small-integers": "Small integers",
    "859-string-interning": "String interning",
    "890-python-internals-project": "Python internals project",
}

DIFFICULTY_WORDS = (
    "intro",
    "basics",
    "first",
)


def read_topics() -> list[tuple[int, str]]:
    """Return every ``number-slug`` pair found in ``structure.a``."""
    text = SOURCE.read_text(encoding="utf-8")
    topics: list[tuple[int, str]] = []
    for line in text.splitlines():
        match = TREE_LINE.match(line) or FLAT_LINE.match(line)
        if match:
            number = int(match.group(1))
            if number:
                topics.append((number, match.group(2)))
    return topics


def section_for(number: int) -> tuple[str, str, str]:
    """Return ``(key, title, blurb)`` for a lesson number."""
    for start, end, key, title in SECTIONS:
        if start <= number <= end:
            return key, title, ""
    raise ValueError(f"lesson {number} belongs to no section")


def humanize(number: int, slug: str) -> str:
    """Turn ``list-slicing`` into ``List slicing``.

    Args:
        number: The lesson number, used to look up a title fix.
        slug: The topic slug from ``structure.a``.

    Returns:
        A title for the lesson.
    """
    key = f"{number:03d}-{slug}"
    if key in TITLE_FIXES:
        return TITLE_FIXES[key]
    words = slug.replace("_", " ").split()
    if words and words[0] in {"if", "else", "for", "not", "is", "in", "and", "or"}:
        words[0] = words[0].capitalize()
    return " ".join(words).capitalize()


def build_module() -> str:
    topics = sorted(set(read_topics()))
    numbers = [number for number, _ in topics]
    expected = list(range(1, 1000))
    if numbers != expected:
        missing = sorted(set(expected) - set(numbers))
        extra = sorted(set(numbers) - set(expected))
        sys.exit(f"structure.a is not 1..999 (missing={missing}, extra={extra})")

    lines: list[str] = [
        '"""Curriculum data for python-from-scratch.',
        "",
        "GENERATED FILE - do not edit by hand.",
        "Run ``python tools/build_curriculum.py`` after changing ``structure.a``.",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "from dataclasses import dataclass",
        "",
        '__all__ = ["Section", "Topic", "SECTIONS", "TOPICS", "LESSONS", "lesson_dir"]',
        "",
        "LESSONS = 'lessons'",
        "",
        "",
        "@dataclass(frozen=True)",
        "class Section:",
        '    """A named range of lesson numbers."""',
        "",
        "    key: str",
        "    title: str",
        "    start: int",
        "    end: int",
        "",
        "",
        "@dataclass(frozen=True)",
        "class Topic:",
        '    """One lesson directory."""',
        "",
        "    number: int",
        "    slug: str",
        "    title: str",
        "    section: str",
        "",
        "    @property",
        "    def folder(self) -> str:",
        '        """Return the directory name, for example ``013-variables``."""',
        '        return f"{self.number:03d}-{self.slug}"',
        "",
    "    @property",
    "    def module(self) -> str:",
    '        """Return the example module name, for example ``lesson_013_variables``."""',
    "        number = f\"{self.number:03d}\"",
    "        words = self.slug.replace(\"-\", \"_\")",
    "        return f\"lesson_{number}_{words}\"",
    "",
        "    @property",
        "    def test_module(self) -> str:",
        '        """Return the test module name for this lesson."""',
        '        return f"test_{self.module}"',
        "",
        "",
        "SECTIONS: tuple[Section, ...] = (",
    ]
    for start, end, key, title in SECTIONS:
        lines.append(f'    Section(key="{key}", title="{title}", start={start}, end={end}),')
    lines.append(")")
    lines.append("")
    lines.append("TOPICS: tuple[Topic, ...] = (")
    for number, slug in topics:
        key, _title, _blurb = section_for(number)
        lines.append(f'    Topic(number={number}, slug="{slug}", title="{humanize(number, slug)}", section="{key}"),')
    lines.append(")")
    lines.append("")
    lines.append("")
    lines.append("def lesson_dir(number: int) -> str:")
    lines.append('    """Return the path of a lesson folder, relative to the repository root."""')
    lines.append("    return f\"{LESSONS}/{number:03d}-{TOPICS[number - 1].slug}\"")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    TARGET.write_text(build_module(), encoding="utf-8")
    print(f"wrote {TARGET.relative_to(ROOT)} with {len(SECTIONS)} sections")


if __name__ == "__main__":
    main()
