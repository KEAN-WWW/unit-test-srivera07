"""This is the starting test file"""
from app.addition import add


def test_addition():
    """Add two numbers"""
    result = add(2, 2)
    assert result == 4
