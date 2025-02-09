from utils import get_choice, clear_screen
from colorama import Fore, Style
from tabulate import tabulate

def set_menu():
    while True:
        clear_screen()
        menu_options = [
            ["1", "Union"],
            ["2", "Intersect"],
            ["3", "Difference"],
            ["4", "Complement"],
            ["5", "Return to Previous Menu"],
        ]
        
        print(Fore.GREEN + "\n\tSet Operations\n" + Style.RESET_ALL)
        print(tabulate(menu_options, headers=["Options", "Operation"], tablefmt="fancy_grid"))
        
        choice = get_choice(1, 5)
        if choice == 5:
            break
        
        sets = create_set()
        if choice == 1:
            result = set_union(sets[0], sets[1])
        elif choice == 2:
            result = set_intersection(sets[0], sets[1])
        elif choice == 3:
            result = set_difference(sets[0], sets[1])
        elif choice == 4:
            result = set_complement(sets[0], sets[1])
            
        if(result is not None):
            print(f"{Fore.CYAN}Result: {result}{Style.RESET_ALL}")
        
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

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
    
    print(f"{Fore.GREEN}Set A : {temp} | Set B : {setB} \nSet A Union with Set B")
    return setA        

def set_intersection(setA: list, setB: list):
    result_set = []

    for val in setA:
        if(val in setB and not result_set.__contains__(val)):
            result_set.append(val)
    
    print(f"{Fore.GREEN}Set A : {setA} | Set B : {setB} \nSet A Intersect with Set B")
    return result_set

def set_difference(setA: list, setB: list):
    result_set = []
    for val in setA:
        if(val not in setB):
            result_set.append(val)
        

    print(f"{Fore.GREEN}Set A : {setA} | Set B : {setB} \nSet A Difference with Set B")
    return result_set
    
def set_complement(setA: list, setB: list):
    result_set = []
    
    for val in setB:
        if(val not in setA):
            result_set.append(val)
                
    print(f"Set A : {setA} | Set B : {setB} \nSet A Complement with Set B = {result_set}")
    return result_set

def create_set():
    print(f"{Fore.CYAN}Create Set")
    sizeA = int(input(f"{Fore.GREEN}Size of Set A: "))
    sizeB = int(input(f"{Fore.GREEN}Size of Set B: "))
    
    setA = []
    setB = []
    
    print(f"{Fore.CYAN}\nCreate Element of Set A")
    for i in range(sizeA):
        val = int(input(f"{Fore.GREEN}Element {i+1} | Value : "))
        setA.append(val)
        
    print(f"{Fore.CYAN}\nCreate Element of Set B")    
    for i in range(sizeB):
        val = int(input(f"{Fore.GREEN}Element {i+1} | Value : "))
        setB.append(val)
        
    return [setA, setB]