from utils import get_choice

def function_menu():
    while True:
        print("\nFunction & Relation Operations:")
        print("(1) Check Function")
        print("(2) Return to Previous Menu")

        choice = get_choice(1, 2)
        if choice == 2:
            break

        if choice == 1:
            check_function()

def check_function():
    print("Checking whether a relation is a function...")
