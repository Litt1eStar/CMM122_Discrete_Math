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
    sizes = get_input_for_matrix_size()    
    input_matrix = create_matrix("Addition", sizes[0], sizes[1], sizes[2], sizes[3])
    addition(input_matrix[0], input_matrix[1])
    
def matrix_subtraction():
    sizes = get_input_for_matrix_size()  
    input_matrix = create_matrix("Subtraction", sizes[0], sizes[1], sizes[2], sizes[3])

def matrix_multiplication():
    sizes = get_input_for_matrix_size()    
    input_matrix = create_matrix("Multiplication", sizes[0], sizes[1], sizes[2], sizes[3])

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
            
    return [first_matrix, second_matrix]

def addition(matrix_a, matrix_b):
    result_matrix = [[0] * len(matrix_a) for _ in range(len(matrix_a[0]))]
    
    for row in range(len(matrix_a)):
        for col in range(len(matrix_a[0])):
            result_matrix[row][col] = matrix_a[row][col] + matrix_b[row][col]
    
def subtraction(matrix_a, matrix_b):
    result_matrix = [[0] * len(matrix_a) for _ in range(len(matrix_a[0]))]
    
    for row in range(len(matrix_a)):
        for col in range(len(matrix_a[0])):
            result_matrix[row][col] = matrix_a[row][col] - matrix_b[row][col]        

def get_input_for_matrix_size():   
    sizex_f = int(input("Maximum Row of First Matrix: "))
    sizey_f = int(input("Maximum Column of First Matrix: "))

    sizex_s = int(input("Maximum Row of Second Matrix: "))
    sizey_s = int(input("Maximum Column of Second Matrix: "))
    
    return [sizex_f, sizey_f, sizex_s, sizey_s]
