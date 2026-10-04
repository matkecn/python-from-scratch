"""Tests for Logging-basics."""

from lesson_591_logging_basics import make_logger, log_a_journey


def test_keeps_steps() -> None:
    """The promise of lesson 'Logging-basics' still holds."""
    assert log_a_journey(["a", "b"]) == ["a", "b"]
