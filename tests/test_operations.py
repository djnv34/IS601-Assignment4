# Test arithmetic operations with parameterized tests.

import pytest
from app.operation.operations import (
    addOperator,
    subtractOperator,
    multiplyOperator,
    divideOperator,
)


@pytest.mark.parametrize("a,b,result", [
    (1, 2, 3),
    (-1, -1, -2),
    (0, 5, 5),
])
def test_add_operator(a, b, result):
    assert addOperator(a, b) == result


@pytest.mark.parametrize("a,b,result", [
    (5, 2, 3),
    (0, 5, -5),
])
def test_subtract_operator(a, b, result):
    assert subtractOperator(a, b) == result


@pytest.mark.parametrize("a,b,result", [
    (2, 3, 6),
    (5, 0, 0),
])
def test_multiply_operator(a, b, result):
    assert multiplyOperator(a, b) == result


def test_divide_operator():
    assert divideOperator(6, 2) == 3


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divideOperator(5, 0)
