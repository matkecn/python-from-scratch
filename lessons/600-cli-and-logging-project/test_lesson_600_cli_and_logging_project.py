"""Tests for Cli-and-logging-project."""

from lesson_600_cli_and_logging_project import make_logger, log_a_journey


def test_keeps_steps() -> None:
    """The promise of lesson 'Cli-and-logging-project' still holds."""
    assert log_a_journey(["a", "b"]) == ["a", "b"]
