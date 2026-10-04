"""Tests for Logging-project."""

from lesson_599_logging_project import make_logger, log_a_journey


def test_keeps_steps() -> None:
    """The promise of lesson 'Logging-project' still holds."""
    assert log_a_journey(["a", "b"]) == ["a", "b"]
