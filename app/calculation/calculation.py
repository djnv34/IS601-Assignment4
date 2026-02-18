# calculation.py
# Defines the Calculation class which represents a single calculation instance.

from app.operation.operations import (
    addOperator,
    subtractOperator,
    multiplyOperator,
    divideOperator,
)


class Calculation:
    # Represents a calculation with two operands and an operation.

    def __init__(self, a: float, b: float, operation: str):
        # Initialize a calculation with two numbers and an operation.
        self.a = a
        self.b = b
        self.operation = operation

    def execute(self) -> float:
        # Execute the calculation based on the selected operation.
        # Demonstrates EAFP (Easier to Ask Forgiveness than Permission).
        try:
            if self.operation == "add":
                return addOperator(self.a, self.b)
            elif self.operation == "subtract":
                return subtractOperator(self.a, self.b)
            elif self.operation == "multiply":
                return multiplyOperator(self.a, self.b)
            elif self.operation == "divide":
                return divideOperator(self.a, self.b)
            else:
                raise ValueError("Invalid operation.") 
        except Exception:
            # Re-raise exception to allow higher-level handling
            raise
