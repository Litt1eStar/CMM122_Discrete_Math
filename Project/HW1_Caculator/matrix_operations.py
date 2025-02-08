from utils import get_choice, print_matrix

def matrix_menu():
    while True:
        print("\nMatrix Operations:")
        print("(1) Addition")
        print("(2) Subtraction")
        print("(3) Multiplication")
        print("(4) Scalar Multiplication")
        print("(5) Transpose of Matrix")
        print("(6) Determinant of Matrix")
        print("(7) Inverse of Matrix")
        print("(8) Eigenvalues and Eigenvectors")
        print("Return to Mainmenu")

        choice = get_choice(1, 9)
        if choice == 8:
            break

        if choice == 1:
            matrix_addition()
        elif choice == 2:
            matrix_subtraction()
        elif choice == 3:
            matrix_multiplication()
        elif choice == 4:
            matrix_scalar_multiplication()
def matrix_addition():
    sizes = get_input_for_matrix_size()    
    input_matrix = create_matrix("Addition", sizes[0], sizes[1], sizes[2], sizes[3])
    
    matrix_a = input_matrix[0]
    matrix_b = input_matrix[1]
    
    result_matrix = [[0] * len(matrix_a) for _ in range(len(matrix_a[0]))]
    
    for row in range(len(matrix_a)):
        for col in range(len(matrix_a[0])):
            result_matrix[row][col] = matrix_a[row][col] + matrix_b[row][col]
    
    print(f"Matrix A : {matrix_a} | Matrix B : {matrix_b} -> Matrix A + Matrix B = {result_matrix}")
def matrix_subtraction():
    sizes = get_input_for_matrix_size()  
    input_matrix = create_matrix("Subtraction", sizes[0], sizes[1], sizes[2], sizes[3])
    
    matrix_a = input_matrix[0]
    matrix_b = input_matrix[1]
    
    result_matrix = [[0] * len(matrix_a) for _ in range(len(matrix_a[0]))]
    
    for row in range(len(matrix_a)):
        for col in range(len(matrix_a[0])):
            result_matrix[row][col] = matrix_a[row][col] - matrix_b[row][col]        

    print(f"Matrix A : {matrix_a} | Matrix B : {matrix_b} -> Matrix A - Matrix B = {result_matrix}")
def matrix_multiplication():
    sizes = get_input_for_matrix_size()    
    input_matrix = create_matrix("Multiplication", sizes[0], sizes[1], sizes[2], sizes[3])
    
    matrix_a = input_matrix[0]
    matrix_b = input_matrix[1]
    
    result_matrix = [[0] * len(matrix_a) for _ in range(len(matrix_b[0]))]
    
    for row in range(len(matrix_a)):
        for col in range(len(matrix_b[0])):
            for k in range(len(matrix_b[0])):
                result_matrix[row][col] += matrix_a[row][k] * matrix_b[k][col]
                
    print(f"Matrix A : {matrix_a} | Matrix B : {matrix_b} -> Matrix A * Matrix B = {result_matrix}")
def matrix_scalar_multiplication():
    sizex = int(input("Maximum Row of Matrix: "))
    sizey = int(input("Maximum Column of Matrix: "))
    
    matrix = [[0] * sizey for _ in range(sizex)]
    
    for row in range(0, sizex):
        for col in range(0, sizey):
            val = int(input(f"Matrix | Enter Value of POsition [{row}][{col}]: "))
            matrix[row][col] = val
    
    scalarVal = int(input("Scalar Value : "))
    
    for row in range(sizex):
        for col in range(sizey):
            matrix[row][col] *= scalarVal
    
    print(f"Result Matrix -> {matrix}")
def matrix_transpose():
    return
def matrix_determinant():
    return
def matrix_inverse():
    return
def matrix_eigenvalues_eigenvectors():
    return
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
def get_input_for_matrix_size():   
    sizex_f = int(input("Maximum Row of First Matrix: "))
    sizey_f = int(input("Maximum Column of First Matrix: "))

    sizex_s = int(input("Maximum Row of Second Matrix: "))
    sizey_s = int(input("Maximum Column of Second Matrix: "))
    
    return [sizex_f, sizey_f, sizex_s, sizey_s]
