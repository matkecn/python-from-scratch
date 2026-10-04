"""Structured-logging.

Logging writes notes about what your program is doing.

Run me:
    python 598-structured-logging/lesson_598_structured_logging.py
"""

from __future__ import annotations


import logging

logger = logging.getLogger("lesson")


def make_logger(level: int = logging.INFO) -> logging.Logger:
    """Return a logger that writes short messages.

    Args:
        level: The lowest level to show.

    Returns:
        The configured logger.
    """
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")
    return logger


def log_a_journey(steps: list[str]) -> list[str]:
    """Log each step and return the steps.

    Args:
        steps: The steps to log.

    Returns:
        The same steps, unchanged.
    """
    for step in steps:
        logger.info("step: %s", step)
    return steps


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    make_logger()
    print(log_a_journey(["start", "stop"]))


if __name__ == "__main__":
    main()
