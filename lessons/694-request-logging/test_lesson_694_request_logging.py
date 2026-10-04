"""Tests for Request-logging."""

from lesson_694_request_logging import make_logger, log_a_journey


def test_keeps_steps() -> None:
    """The promise of lesson 'Request-logging' still holds."""
    assert log_a_journey(["a", "b"]) == ["a", "b"]
