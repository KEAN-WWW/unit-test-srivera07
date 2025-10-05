"""Tests for subtraction module."""

from app.subtraction import subtract


def test_subtraction():
    """Test subtracting two numbers."""
    result = subtract(4, 2)
    assert result == 2
    assert subtract(10, 5) == 5
    assert subtract(0, 0) == 0
