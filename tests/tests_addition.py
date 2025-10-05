"""This is the starting test file"""
from app.division import divide

def test_division():
    """Add two numbers"""
    result = divide(2, 2)
    assert result == 1
