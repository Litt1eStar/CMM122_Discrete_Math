from utils import get_choice, clear_screen
from colorama import Fore, Style
from tabulate import tabulate

def function_menu():
    while True:
        clear_screen()
        menu_options = [
            ["1", "Is Function"],
            ["2", "Find Domain and Range"],
            ["3", "Determine Injective Function (ONE TO ONE)"],
            ["4", "Determine Surjective Function (MANY TO ONE)"],
            ["5", "Find Inverse Relation"],
            ["6", "Return to Previous Menu"]
        ]
        
        print(Fore.GREEN + "\n\t\tFunction and Relation\n" + Style.RESET_ALL)
        print(tabulate(menu_options, headers=["Options", "Operation"], tablefmt="heavy_outline"))

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
            inverse_relation()

def isFunction(set_to_check = None):
    if(set_to_check == None):
        set_to_check = create_single_relation()
    
    temp_domain = -1
    isFunction = True
    for coordinate in set_to_check:
        if(coordinate[0]==temp_domain):
            isFunction = False
        else:
            temp_domain = coordinate[0]

    if(isFunction):
        print(f"{set_to_check} is Function")
        return True
    else:
        print(f"{set_to_check} is not Function")        
        return False
    
def domain_and_range(set = None):
    if(set == None):
        set = create_single_relation()
        
    setDomain = list()
    setRange = list()

    for val in set:
        setDomain.append(val[0])
        setRange.append(val[1])
    
    print(f"Set: {set} | Domain: {setDomain}, Range: {setRange}")
    return [setDomain, setRange]
    
def is_injective_function(set = None):
    if(set == None):
        set = create_single_relation()
    set_data = domain_and_range(set)
    set_domain = set_data[0]
    set_range = set_data[1]
    
    seen = {*{}}
    for i in range(len(set_domain)):
        if set_range[i] in seen:
            print(f"Set: {set} | Injective Set ? : False")
            return False
        seen.add(set_range[i])
    print(f"Set: {set} | Injective Set ? : True")
    return True

def is_surjective_function(set = None):
    if(set == None):
        set = create_single_relation()
    set_data = domain_and_range(set)
    set_domain = set_data[0]
    set_range = set_data[1]

    seen = {*{}}
    for i in range(len(set_domain)):
        if set_range[i] in seen:
            print(f"Set: {set} | Surjective Set ? : True")
            return True
        seen.add(set_range[i])
    print(f"Set: {set} | Surjective Set ? : False")
    return False

def inverse_relation(set = None):
    if(set==None):
        set = create_single_relation()
    inverse_relation = {*{}}
    
    for x,y in set:
        inverse_relation.add((y, x))
        
    print(f"Relation: {set} | Inverse of Relation: {inverse_relation}")
    return inverse_relation
    
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