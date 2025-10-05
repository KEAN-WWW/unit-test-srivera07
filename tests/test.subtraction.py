"""This is the starting test file"""
from app.subtraction import subtract


def test_subtraction():
    """Add two numbers"""
    result = subtract(2, 2)
    assert result == 0
