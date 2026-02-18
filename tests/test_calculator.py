# Tests for Calculator class.

from app.calculator.calculator import Calculator


def test_perform_calculation():
    calc = Calculator()
    result = calc.perform_calculation(2, 3, "multiply")
    assert result == 6
    assert len(calc.get_history()) == 1
