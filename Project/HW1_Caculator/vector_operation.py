from utils import get_choice, clear_screen
from colorama import Fore, Style
from tabulate import tabulate

def vector_menu():
    while True:
        clear_screen()
        menu_options = [
            ["1", "Addtion"],
            ["2", "Subtraction"],
            ["3", "Scalar Multiplication"],
            ["4", "Dot Product"],
            ["5", "Cross Product"],
            ["6", "Return to Previous Menu"]
        ]
        
        print(Fore.GREEN + "\n\tVector Operations\n" + Style.RESET_ALL)
        print(tabulate(menu_options, headers=["Options", "Operation"], tablefmt="fancy_grid"))
        
        choice = get_choice(1, 6)
        if choice == 6:
            break
        
        if choice == 1:            
            result = vector_addition()
        elif choice == 2:
            result = vector_subtraction()
        elif choice == 3:
            result = vector_scalar_multiplication()
        elif choice == 4:
            result = vector_dot_product()
        elif choice == 5:
            result = vector_cross_product()
            
        if(result is not None):
            print(f"{Fore.CYAN}Result: {result}{Style.RESET_ALL}")
        
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
            
def vector_addition(vectors = None):
    if(vectors == None):
        vectors = create_two_vector()
    
    vector_a = vectors[0]
    vector_b = vectors[1]
    
    if(len(vector_a) != len(vector_b)):
        print(f"{Fore.RED}Vector have to be same size")
        return
    
    result_vector = []
    for i in range(len(vector_a)):result_vector.append(vector_a[i] + vector_b[i])
    print(f"{Fore.GREEN}Result Vector:")
    return result_vector
    
def vector_subtraction(vectors = None):
    if(vectors == None):
        vectors = create_two_vector()
    
    vector_a = vectors[0]
    vector_b = vectors[1]
    
    if(len(vector_a) != len(vector_b)):
        print(f"{Fore.RED}Vector have to be same size")
        return
    
    result_vector = []
    for i in range(len(vector_a)):result_vector.append(vector_a[i] - vector_b[i])
    print(f"{Fore.GREEN}Result Vector:")
    return result_vector

def vector_scalar_multiplication(vector_a = None, scalar_value = None):
    if(vector_a == None):
        vector_a = create_single_vector()
    
    if(scalar_value == None):
        scalar_value = int(input(f"{Fore.GREEN}Scalar Value for Multiply to Vector: "))
    
    for i in range(len(vector_a)):vector_a[i] *= scalar_value
    print(f"{Fore.GREEN}Result Vector:")
    return vector_a
    
def vector_dot_product(vectors = None):
    if(vectors==None):
        vectors = create_two_vector()
    
    vector_a = vectors[0]
    vector_b = vectors[1]

    if(len(vector_a) != len(vector_b)):
        print(f"{Fore.RED}Vector have to be same size")
        return

    result = 0
    for i in range(len(vector_a)):result+=vector_a[i]*vector_b[i]
    
    print(f"Vector A: {vector_a}, Vector B: {vector_b}")
    print(f"Dot Product")
    return result

def vector_cross_product(vectors = None):
    if(vectors == None):
        vectors = create_two_vector()
    
    vector_a = vectors[0]
    vector_b = vectors[1]

    if len(vector_a) != 3 or len(vector_b) != 3:
        print("Cross product is only defined for 3-dimensional vectors")
        return

    result_vector = [
        vector_a[1] * vector_b[2] - vector_a[2] * vector_b[1],  
        vector_a[2] * vector_b[0] - vector_a[0] * vector_b[2],  
        vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0]   
    ]
    
    print(f"Cross Product")
    
    return result_vector

def create_two_vector():
    print(f"{Fore.CYAN}Create Vector")
    size_of_vector = int(input(f"{Fore.GREEN}Size of Vector(2, 3): "))

    if size_of_vector not in [2,3]:
        print(f"{Fore.RED}This program support only 2D and 3D Matrix")
        return
    
    vector_a = []
    vector_b = []
    
    print(f"{Fore.CYAN}Create Value of Vector A")
    for i in range(size_of_vector):
        vector_index = 'i' if i == 0 else 'j' if i == 1 else 'k' if i == 2 else None
        val = int(input(f"{Fore.GREEN}First Vector | {vector_index}: "))
        vector_a.append(val)
        
    print(f"{Fore.CYAN}Create Value of Vector B")
    for i in range(size_of_vector):
        vector_index = 'i' if i == 0 else 'j' if i == 1 else 'k' if i == 2 else None
        val = int(input(f"{Fore.GREEN}Second Vector | {vector_index}: "))
        vector_b.append(val)
    
    return [vector_a, vector_b]
        
def create_single_vector():
    print(f"{Fore.CYAN}Create Vector")
    size_of_vector = int(input(f"{Fore.GREEN}Size of Vector(2, 3): "))
    
    if size_of_vector not in [2,3]:
        print(f"{Fore.RED}This program support only 2D and 3D Matrix")
        return
    
    vector_a = []
    
    print(f"{Fore.CYAN}Create Value of Vector A")
    for i in range(size_of_vector):
        vector_index = 'i' if i == 0 else 'j' if i == 1 else 'k' if i == 2 else None
        val = int(input(f"{Fore.GREEN}First Vector | {vector_index}: "))
        vector_a.append(val)
        
    return vector_a