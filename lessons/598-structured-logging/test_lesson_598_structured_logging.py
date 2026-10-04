"""Tests for Structured-logging."""

from lesson_598_structured_logging import make_logger, log_a_journey


def test_keeps_steps() -> None:
    """The promise of lesson 'Structured-logging' still holds."""
    assert log_a_journey(["a", "b"]) == ["a", "b"]
