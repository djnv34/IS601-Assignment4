# operations.py
# Cntains basic arithmetic operation functions.
# Each operator performs a different mathematical operation.


def addOperator(a: float, b: float) -> float:
    # Return the sum of two numbers.
    return a + b


def subtractOperator(a: float, b: float) -> float:
    # Return the difference between two numbers.
    return a - b


def multiplyOperator(a: float, b: float) -> float:
    # Return the product of two numbers.
    return a * b


def divideOperator(a: float, b: float) -> float:
    # Return the division of two numbers.
    # Uses LBYL (Look Before You Leap) to prevent division by zero.
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

