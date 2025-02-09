from utils import get_choice

def function_menu():
    while True:
        print("\nFunction & Relation Operations:")
        print("(1) Is Function")
        print("(2) Find Domain and Range")
        print("(3) Determine Injective Function(ONE TO ONE)")
        print("(4) Determine Surjective Function(MANY TO ONE)")
        print("(5) Find Inverse Relation")
        print("(6) Return to Previous Menu")

        choice = get_choice(1, 6)
        if choice == 6:
            break

        if choice == 1:
            isFunction()
        elif choice == 2:
            domain_and_range()
        elif choice == 3:
            is_injective_function()
        elif choice == 4:
            is_surjective_function()
        elif choice == 5:
            inverse_function()

def isFunction():
    set_to_check = create_single_relation()
    
    temp_domain = -1
    isFunction = True
    for coordinate in set_to_check:
        if(coordinate[0]==temp_domain):
            isFunction = False
        else:
            temp_domain = coordinate[0]

    if(isFunction): print(f"{set_to_check} is Function")
    else: print(f"{set_to_check} is not Function")        

def domain_and_range():
    set = create_single_relation()
    setDomain = []
    setRange = []

    for val in set:
        setDomain.append(val[0])
        setRange.append(val[1])
    
    print(f"Set: {set} | Domain: {setDomain}, Range: {setRange}")
def is_injective_function():
    return

def is_surjective_function():
    return

def inverse_function():
    return

def create_single_relation():
    size = int(input("Size of relation you want to create: "))
    set = {*{}}
    for i in range(size):
        xVal = int(input(f"Element {i+1} | Value x: "))
        yVal = int(input(f"Element {i+1} | Value y: "))
        set.add((xVal, yVal))
    return set

def create_two_relation():
    sizef = int(input("Size of first relation: "))
    sizes = int(input("Size of second relation: "))
    
    setf = {*{}}
    sets = {*{}}
    
    for i in range(sizef):
        xVal = int(input(f"First Set | Element {i+1} | Value x: "))
        yVal = int(input(f"First Set | Element {i+1} | Value y: "))
    setf.add((xVal, yVal))

    for i in range(sizes):
        xVal = int(input(f"Second Set | Element {i+1} | Value x: "))
        yVal = int(input(f"Second Set | Element {i+1} | Value y: "))
    sets.add((xVal, yVal))

    return [setf, sets] 