from utils import get_choice

def matrix_menu():
    while True:
        print("\nMatrix Operations:")
        print("(1) Addition")
        print("(2) Subtraction")
        print("(3) Multiplication")
        print("(4) Return to Previous Menu")

        choice = get_choice(1, 4)
        if choice == 4:
            break

        if choice == 1:
            matrix_addition()
        elif choice == 2:
            matrix_subtraction()
        elif choice == 3:
            matrix_multiplication()

def matrix_addition():
    print("Performing Matrix Addition...")

def matrix_subtraction():
    print("Performing Matrix Subtraction...")

def matrix_multiplication():
    print("Performing Matrix Multiplication...")
