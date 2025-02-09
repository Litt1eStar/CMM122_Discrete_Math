from utils import get_choice
from colorama import Fore, Style
from tabulate import tabulate

def set_menu():
    while True:
        menu_options = [
            ["1", "Union"],
            ["2", "Intersect"],
            ["3", "Difference"],
            ["4", "Complement"],
            ["5", "Return to Previous Menu"],
        ]
        
        print(Fore.GREEN + "\n\tSet Operations\n" + Style.RESET_ALL)
        print(tabulate(menu_options, headers=["Options", "Operation"], tablefmt="heavy_outline"))
        
        choice = get_choice(1, 5)
        if choice == 5:
            break
        
        sets = create_set()
        if choice == 1:
            set_union(sets[0], sets[1])
        elif choice == 2:
            set_intersection(sets[0], sets[1])
        elif choice == 3:
            set_difference(sets[0], sets[1])
        elif choice == 4:
            set_complement(sets[0], sets[1])

def set_union(setA: list, setB: list):      
    temp = setA  
    #Merge 2 set together
    for val in setB:
        setA.append(val)
        
    #Then Sorting it using Bubble Sort Algorithm
    for i in range(len(setA)):
        for j in range(len(setA) - i - 1):
            if(setA[j] > setA[j+1]):
                setA[j], setA[j+1] = setA[j+1], setA[j]
    
    print(f"Set A : {temp} | Set B : {setB} \nSet A Union with Set B = {setA}")
    return setA        

def set_intersection(setA: list, setB: list):
    result_set = []

    for val in setA:
        if(val in setB and not result_set.__contains__(val)):
            result_set.append(val)
    
    print(f"Set A : {setA} | Set B : {setB} \nSet A Intersect with Set B = {result_set}")
    return result_set

def set_difference(setA: list, setB: list):
    result_set = []
    for val in setA:
        if(val not in setB):
            result_set.append(val)
        

    print(f"Set A : {setA} | Set B : {setB} \nSet A Difference with Set B = {result_set}")
    return result_set
    
def set_complement(setA: list, setB: list):
    result_set = []
    
    for val in setB:
        if(val not in setA):
            result_set.append(val)
                
    print(f"Set A : {setA} | Set B : {setB} \nSet A Complement with Set B = {result_set}")
    return result_set

def create_set():
    sizeA = int(input("Size of Set A: "))
    sizeB = int(input("Size of Set B: "))
    
    setA = []
    setB = []
    
    for i in range(sizeA):
        val = int(input(f"Element {i} | Value : "))
        setA.append(val)
        
    for i in range(sizeB):
        val = int(input(f"Element {i} | Value : "))
        setB.append(val)
        
    return [setA, setB]