# calculator.py
# Main calculator application implementing:
# - REPL interface
# - Calculation history
# - Command handling
# - Input validation

from app.calculation.calculation_factory import CalculationFactory


class Calculator:
    # Command-line calculator application.

    def __init__(self):
        # Initialize calculator with empty history.
        self.history = []

    def perform_calculation(self, a: float, b: float, operation: str) -> float:
        # Perform a calculation and store result in history.
        calculation = CalculationFactory.create_calculation(a, b, operation)
        result = calculation.execute()

        # Store the calculation in history as a tuple.
        self.history.append((a, operation, b, result))

        return result

    def get_history(self):
        # Return calculation history.
        return self.history

    def repl(self):
        # Read-Eval-Print Loop (REPL) for user interaction.
        print("Welcome to the Professional Calculator!")
        print("Type 'help' for available commands.")

        while True:
            user_input = input(">>> ").strip()

            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            elif user_input.lower() == "help":
                print("Available operations: add, subtract, multiply, divide")
                print("Usage: operation number1 number2")
                print("Special commands: help, history, exit")

            elif user_input.lower() == "history":
                for entry in self.history:
                    print(entry)

            else:
                parts = user_input.split()

                # LBYL: Validate correct number of arguments
                if len(parts) != 3:
                    print("Invalid format. Use: operation number1 number2")
                    continue  # pragma: no cover

                operation, a_str, b_str = parts

                try:
                    # EAFP: Attempt to convert inputs
                    a = float(a_str)
                    b = float(b_str)

                    result = self.perform_calculation(a, b, operation)
                    print("Result:", result)

                except ValueError as e:
                    print("Error:", e)

                if __name__ == "__main__":
                    calculator = Calculator()
                    calculator.repl()
