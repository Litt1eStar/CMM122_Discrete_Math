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
    set_to_check = create_set()
    
def create_set():
    size = int(input("Size of Set you want to create: "))
    set = {*{}}
    for i in range(size):
        val = int(input("Value to Insert to new set: "))
        set.add(val)
    return set

