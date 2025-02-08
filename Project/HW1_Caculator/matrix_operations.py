from utils import get_choice, print_matrix

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
    sizex_f = int(input("Maximum Row of First Matrix: "))
    sizey_f = int(input("Maximum Column of First Matrix: "))

    sizex_s = int(input("Maximum Row of Second Matrix: "))
    sizey_s = int(input("Maximum Column of Second Matrix: "))
    
    create_matrix("Addition", sizex_f, sizey_f, sizex_s, sizey_s)
    
def matrix_subtraction():
    print("Performing Matrix Subtraction...")

def matrix_multiplication():
    print("Performing Matrix Multiplication...")
    sizex_f = int(input("Maximum Row of First Matrix: "))
    sizey_f = int(input("Maximum Column of First Matrix: "))

    sizex_s = int(input("Maximum Row of Second Matrix: "))
    sizey_s = int(input("Maximum Column of Second Matrix: "))
    
    create_matrix("Multiplication", sizex_f, sizey_f, sizex_s, sizey_s)
    
def create_matrix(op ,sizex_f, sizey_f, sizex_s, sizey_s):
    is_valid = False
    err_msg = ""
    if op == "Addition" or op == "Subtraction":
        is_valid = (sizex_f == sizex_s) and (sizey_f == sizey_s)
        err_msg = "These two matrices must have same dimension for addition or subtraction0"
    elif op == "Multiplication":
        is_valid = sizey_f == sizex_s
        err_msg = "These two matrices can't be multiplied"        
    if(not is_valid):
        print(err_msg)
        return

    first_matrix = [[0] * sizey_f for _ in range(sizex_f)]
    second_matrix = [[0] * sizey_s for _ in range(sizex_s)]
    
    for row in range(0, sizex_f):
        for col in range(0, sizey_f):
            val = int(input(f"First Matrix | Enter Value of Position [{row}][{col}]: "))
            first_matrix[row][col] = val
            
    for row in range(0, sizex_s):
        for col in range(0, sizey_s):
            val = int(input(f"Second Matrix | Enter Value of Position [{row}][{col}]: "))
            second_matrix[row][col] = val

