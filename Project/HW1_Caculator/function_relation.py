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
    set_to_check = create_relation()
    
    temp_domain = -1
    isFunction = True
    for coordinate in set_to_check:
        if(coordinate[0]==temp_domain):
            isFunction = False
        else:
            temp_domain = coordinate[0]

    if(isFunction): print(f"{set_to_check} is Function")
    else: print(f"{set_to_check} is not Function")        

def create_relation():
    size = int(input("Size of relation you want to create: "))
    set = {*{}}
    for i in range(size):
        xVal = int(input(f"Element {i+1} | Value x: "))
        yVal = int(input(f"Element {i+1} | Value y: "))
        set.add((xVal, yVal))
    return set
    

