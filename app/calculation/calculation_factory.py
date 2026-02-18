# calculation_factory.py
# Calculation objects factory implementation. Responsible for creating Calculation instances.

from app.calculation.calculation import Calculation


class CalculationFactory:
    # Factory class responsible for creating Calculation instances.

    @staticmethod
    def create_calculation(a: float, b: float, operation: str) -> Calculation:
        # Create and return a Calculation object.
        return Calculation(a, b, operation)
