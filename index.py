import numpy as np

def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Normal Calculator")
        print("2. Matrix Calculator")
        print("3. Complex Number Calculator")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            normal_calculator()
        elif choice == "2":
            matrix_calculator()
        elif choice == "3":
            complex_calculator()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

# Normal Calculator
def normal_calculator():
    while True:
        print("\n--- Normal Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            calculate("+")
        elif choice == "2":
            calculate("-")
        elif choice == "3":
            calculate("*")
        elif choice == "4":
            calculate("/")
        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")

def calculate(operation):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "+":
        print(f"Result: {num1 + num2}")
    elif operation == "-":
        print(f"Result: {num1 - num2}")
    elif operation == "*":
        print(f"Result: {num1 * num2}")
    elif operation == "/":
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Division by zero is undefined!")

# Matrix Calculator
def matrix_calculator():
    while True:
        print("\n--- Matrix Calculator ---")
        print("1. Matrix Addition")
        print("2. Matrix Subtraction")
        print("3. Matrix Multiplication")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            matrix_operation("add")
        elif choice == "2":
            matrix_operation("subtract")
        elif choice == "3":
            matrix_operation("multiply")
        elif choice == "4":
            transpose_matrix()
        elif choice == "5":
            determinant_matrix()
        elif choice == "6":
            break
        else:
            print("Invalid choice, try again.")

def matrix_operation(operation):
    matrix1 = input_matrix("Matrix 1")
    matrix2 = input_matrix("Matrix 2")

    if matrix1.shape != matrix2.shape and operation in ["add", "subtract"]:
        print("Error: Matrices must have the same dimensions for addition or subtraction.")
        return

    try:
        if operation == "add":
            result = np.add(matrix1, matrix2)
        elif operation == "subtract":
            result = np.subtract(matrix1, matrix2)
        elif operation == "multiply":
            if matrix1.shape[1] != matrix2.shape[0]:
                print("Error: The number of columns in Matrix 1 must equal the number of rows in Matrix 2 for multiplication.")
                return
            result = np.dot(matrix1, matrix2)
        print("Result:",result)
    except ValueError:
        print("Invalid matrix operation!")

def transpose_matrix():
    matrix = input_matrix("Matrix")
    result = np.transpose(matrix)
    print(f"Transpose:\n{result}")

def determinant_matrix():
    matrix = input_matrix("Square Matrix")
    if matrix.shape[0] != matrix.shape[1]:
        print("Error: Matrix must be square to calculate the determinant.")
        return
    try:
        result = np.linalg.det(matrix)
        print(f"Determinant: {result}")
    except np.linalg.LinAlgError:
        print("Error calculating determinant.")

def input_matrix(name):
    rows = int(input(f"Enter the number of rows for {name}: "))
    cols = int(input(f"Enter the number of columns for {name}: "))
    matrix = []

    print(f"Enter elements for {name} row by row (space-separated):")
    for i in range(rows):
        while True:  # Ensure valid row input
            row = input(f"Row {i + 1}: ").split()
            if len(row) != cols:
                print(f"Error: You must enter exactly {cols} elements.")
            else:
                try:
                    matrix.append([float(num) for num in row])
                    break
                except ValueError:
                    print("Error: All elements must be numbers.")

    return np.array(matrix)

# Complex Number Calculator
def complex_calculator():
    while True:
        print("\n--- Complex Number Calculator ---")
        print("1. Complex Addition")
        print("2. Complex Subtraction")
        print("3. Complex Multiplication")
        print("4. Complex Division")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            complex_operation("+")
        elif choice == "2":
            complex_operation("-")
        elif choice == "3":
            complex_operation("*")
        elif choice == "4":
            complex_operation("/")
        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")

def complex_operation(operation):
    num1 = complex(input("Enter first complex number (in form a+bj): "))
    num2 = complex(input("Enter second complex number (in form a+bj): "))

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Division by zero is undefined!")
            return

    print(f"Result: {format_complex(result)}")

def format_complex(number):
    real_part = number.real
    imag_part = number.imag
    # Format the output to remove '+-' cases and handle real or imaginary zeroes
    if imag_part >= 0:
        return f"{real_part}+{imag_part}j"
    else:
        return f"{real_part}{imag_part}j"

# Start the program
if __name__ == "__main__":
    main_menu()
