# Python Basic Calculator
# Author: Exequiel
# Simple console-based calculator with error handling

# --- Basic arithmetic functions ---
def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """
    Return the quotient of a and b.
    If b is zero, return an error message.
    """
    if b == 0:
        return "Error: Cannot divide by 0"
    return a / b

# --- Main program loop ---
while True:
    print("\nPython Basic Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    option = input("Choose an option (1-5): ")

    # Exit option
    if option == "5":
        print("Exiting the calculator...")
        break

    # Invalid option check
    if option not in ["1", "2", "3", "4"]:
        print("Invalid option, please try again.")
        continue

    # Input numbers with error handling
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: You must enter valid numbers.")
        continue

    # Execute the selected operation
    if option == "1":
        print("Result:", add(num1, num2))
    elif option == "2":
        print("Result:", subtract(num1, num2))
    elif option == "3":
        print("Result:", multiply(num1, num2))
    elif option == "4":
        print("Result:", divide(num1, num2))