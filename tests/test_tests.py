import pytest


def add(a, b):
    return a + b

def div(a, b):
    return a / b

@pytest.mark.parametrize("num1, num2, res",[
    (1, 1, 2),
    (11.2, 12, 23.2),
    (15, 15, 30),
    (0, 0, 0)
])
def test_add(num1, num2, res):
    assert add(num1, num2) == res

@pytest.mark.parametrize("num1, num2, res",[
    (1, 1, 1),
    (10, 2, 5),
    (8, 4, 2)
])
def test_div(num1, num2, res):
    assert div(num1, num2) == res

def test_div_failure():
    with pytest.raises(ZeroDivisionError):
        div(2, 0)