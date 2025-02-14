from utils import get_choice, clear_screen
from colorama import Fore, Style
from tabulate import tabulate

def function_menu():
    while True:
        clear_screen()
        menu_options = [
            ["1", "Is Function"],
            ["2", "Find Domain and Range"],
            ["3", "Find Inverse Relation"],
            ["4", "Return to Previous Menu"]
        ]
        
        print(Fore.GREEN + "\n\t\tFunction and Relation\n" + Style.RESET_ALL)
        print(tabulate(menu_options, headers=["Options", "Operation"], tablefmt="fancy_grid"))

        choice = get_choice(1, 4)
        if choice == 4:
            break

        if choice == 1:
            result = isFunction()
        elif choice == 2:
            result = domain_and_range()
        elif choice == 3:
            result = inverse_relation()
            
        if result is not None:
            print(f"{Fore.CYAN}\nResult: {result}{Style.RESET_ALL}")
            
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

def isFunction(set_to_check = None):
    if set_to_check is None:
        set_to_check = create_single_relation()
    
    seen_inputs = set()
    
    for coordinate in set_to_check:
        if len(coordinate) != 2:
            print(f"{Fore.RED}Invalid coordinate format: {coordinate}. Expected a tuple (input, output).")
            return False
        
        input_value = coordinate[0]
        
        if input_value in seen_inputs:
            print(f"{Fore.RED}{set_to_check} is not a function (duplicate input: {input_value})")
            return False
        seen_inputs.add(input_value)
    
    print(f"{Fore.GREEN}{set_to_check} is a function.")
    return True

    
def domain_and_range(set = None):
    if(set == None):
        set = create_single_relation()
        
    setDomain = list()
    setRange = list()

    for val in set:
        setDomain.append(val[0])
        setRange.append(val[1])
    
    print(f"{Fore.CYAN}Data")
    print(f"{Fore.GREEN}Set: {set} | Domain: {setDomain}, Range: {setRange}")
    return [setDomain, setRange]
    
def inverse_relation(set = None):
    if(set==None):
        set = create_single_relation()
    inverse_relation = {*{}}
    
    for x,y in set:
        inverse_relation.add((y, x))
    
    print(f"{Fore.CYAN}Relation: {set}")
    print(f"{Fore.GREEN}Inverse of Relation: ")
    return inverse_relation
    
def create_single_relation():
    print(f"{Fore.CYAN}Create Relation")
    size = int(input(f"{Fore.GREEN}Size of relation you want to create: "))
    set = {*{}}
    print(f"{Fore.CYAN}Create Element in Set")
    for i in range(size):
        xVal = int(input(f"Element {i+1} | Value x: "))
        yVal = int(input(f"Element {i+1} | Value y: "))
        set.add((xVal, yVal))
    return set

def create_two_relation():
    print(f"{Fore.CYAN}Create Relation")
    sizef = int(input(f"{Fore.GREEN}Size of first relation: "))
    sizes = int(input(f"{Fore.GREEN}Size of second relation: "))
    
    setf = {*{}}
    sets = {*{}}
    
    print(f"{Fore.CYAN}Create Element in First Set")    
    for i in range(sizef):
        xVal = int(input(f"First Set | Element {i+1} | Value x: "))
        yVal = int(input(f"First Set | Element {i+1} | Value y: "))
    setf.add((xVal, yVal))

    print(f"{Fore.CYAN}Create Element in Second Set")
    for i in range(sizes):
        xVal = int(input(f"Second Set | Element {i+1} | Value x: "))
        yVal = int(input(f"Second Set | Element {i+1} | Value y: "))
    sets.add((xVal, yVal))

    return [setf, sets] 