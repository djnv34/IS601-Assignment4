# Tests for Calculation and Factory classes.

import pytest
from app.calculation.calculation import Calculation
from app.calculation.calculation_factory import CalculationFactory


def test_factory_creates_calculation():
    calc = CalculationFactory.create_calculation(1, 2, "add")
    assert calc.a == 1
    assert calc.b == 2
    assert calc.operation == "add"


def test_execute_add():
    calc = CalculationFactory.create_calculation(1, 2, "add")
    assert calc.execute() == 3


def test_invalid_operation():
    calc = CalculationFactory.create_calculation(1, 2, "invalid")
    with pytest.raises(ValueError):
        calc.execute()

