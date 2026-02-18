from app.calculator.calculator import Calculator


def main():
    calc = Calculator()
   

    while True:
        print("\n\n\n___________________________________________________")
        print("\nWelcome to the Interactive Command-Line CALCULATOR!")
        print("___________________________________________________")
        print("\nOperations: add, subtract, multiply, divide")
        print("Type 'exit' to quit.")
        print("___________________________________________________")

        operation = input("Enter operation: ").strip().lower()

        if operation == "exit":
            print("Goodbye!")
            break

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = calc.perform_calculation(a, b, operation)
            print("___________________________________________________")
            print(f"Result: {result}")
        except ValueError as e:
            print("___________________________________________________")
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
