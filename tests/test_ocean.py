"""Test the ocean module."""

from riskcraft.ocean import foo


## Test the foo function
def test_foo():
    """Test the foo function."""
    assert foo(1, 2) == 3
    assert foo(2, 3) == 5
    assert foo(3, 4) == 7
