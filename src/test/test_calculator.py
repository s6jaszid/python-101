"""
This is the calculator test file
"""

import pytest
from ..calculator import add, divide


# this is an example
def test_add():
    assert add(0, 0) == 0, "result not correct"
    assert add(1, 2) == 3, "result not correct"


# add your tests here
def test_divide():
    assert divide(1, 1) == 1, "result not correct"
    assert divide(10, 2) == 5, "result not correct"
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
