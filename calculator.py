import math

# Enhanced calculator with more operations and error handling
def calculator():
    memory = None  # Store the last result in memory

    while True:
        print("\nSelect an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponentiation")
        print("6. Modulo")
        print("7. Square Root")
        print("8. View History")
        print("9. Exit")

        operation = input("Enter the operation (1-9): ")

        if operation == '9':
            print("Goodbye!")
            break  # Exit the loop

        if operation == '8':  # View calculation history
            print(f"Last result: {memory}")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue  # Go back to the operation menu

        if operation == '1':
            result = num1 + num2
            print(f"The result of addition is: {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"The result of subtraction is: {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"The result of multiplication is: {result}")
        elif operation == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"The result of division is: {result}")
            else:
                print("Error! Division by zero.")
                continue
        elif operation == '5':  # Exponentiation
            result = num1 ** num2
            print(f"The result of exponentiation is: {result}")
        elif operation == '6':  # Modulo
            result = num1 % num2
            print(f"The result of modulo is: {result}")
        elif operation == '7':  # Square Root (of first number)
            if num1 >= 0:
                result = math.sqrt(num1)
                print(f"The square root of {num1} is: {result}")
            else:
                print("Error! Cannot take the square root of a negative number.")
                continue
        else:
            print("Invalid operation! Please select a valid operation.")
            continue

        # Store the result in memory
        memory = result