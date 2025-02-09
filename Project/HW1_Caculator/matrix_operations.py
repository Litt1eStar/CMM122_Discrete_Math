from utils import get_choice, print_matrix
from colorama import Fore, Style
from tabulate import tabulate

def matrix_menu():
    while True:
        menu_options = [
            ["1", "Addition"],
            ["2", "Subtraction"],
            ["3", "Multiplication"],
            ["4", "Scalar Multiplication"],
            ["5", "Transpose"],
            ["6", "Determinant"],
            ["7", "Inverse"],
            ["8", "Exit"]
        ]

        print(Fore.GREEN + "\n\tMatrix Operations\n" + Style.RESET_ALL)
        print(tabulate(menu_options, headers=["Option", "Operation"], tablefmt="heavy_outline"))


        choice = get_choice(1, 8)
        if choice == 8:
            break

        if choice == 1:
            result = matrix_addition()
        elif choice == 2:
            matrix_subtraction()
        elif choice == 3:
            matrix_multiplication()
        elif choice == 4:
            matrix_scalar_multiplication()
        elif choice == 5:
            result = matrix_transpose()
            print(f"Transpose of Matrix = {result}")
        elif choice == 6:
            matrix_determinant()
        elif choice == 7:
            result = matrix_inverse()
            print(f"Inverse of Matrix = {result}")
            
def matrix_addition(matrix_a = None, matrix_b = None):
    if(matrix_a == None and matrix_b == None):
        sizes = get_input_for_matrix_size()    
        input_matrix = create_matrix("Addition", sizes[0], sizes[1], sizes[2], sizes[3])
        
        matrix_a = input_matrix[0]
        matrix_b = input_matrix[1]
        
    result_matrix = [[0] * len(matrix_a) for _ in range(len(matrix_a[0]))]
    
    for row in range(len(matrix_a)):
        for col in range(len(matrix_a[0])):
            result_matrix[row][col] = matrix_a[row][col] + matrix_b[row][col]
    
    print(f"Matrix A : {matrix_a} | Matrix B : {matrix_b} -> Matrix A + Matrix B = {result_matrix}")
    return result_matrix
    
def matrix_subtraction(matrix_a = None, matrix_b = None):
    if(matrix_a == None and matrix_b == None):
        sizes = get_input_for_matrix_size()  
        input_matrix = create_matrix("Subtraction", sizes[0], sizes[1], sizes[2], sizes[3])
        
        matrix_a = input_matrix[0]
        matrix_b = input_matrix[1]
    
    result_matrix = [[0] * len(matrix_a) for _ in range(len(matrix_a[0]))]
    
    for row in range(len(matrix_a)):
        for col in range(len(matrix_a[0])):
            result_matrix[row][col] = matrix_a[row][col] - matrix_b[row][col]        

    print(f"Matrix A : {matrix_a} | Matrix B : {matrix_b} -> Matrix A - Matrix B = {result_matrix}")
    return result_matrix

def matrix_multiplication(matrix_a = None, matrix_b = None):
    if(matrix_a == None and matrix_b == None):
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
    return result_matrix
    
def matrix_scalar_multiplication(matrix = None, scalarVal = None):
    if(matrix == None):
        matrix = create_single_matrix()
    
    if(scalarVal == None):
        scalarVal = int(input("Scalar Value : "))
    
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            matrix[row][col] *= scalarVal
    
    print(f"Result Matrix -> {matrix}")
    return matrix
    
def matrix_transpose(matrix = None):
    if(matrix == None):
        matrix = create_single_matrix()

    result_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            result_matrix[col][row] = matrix[row][col]
    
    print(f"Matrix: {matrix} -> Transpose Matrix: {result_matrix}")
    return result_matrix
    
def matrix_determinant(matrix = None):
    if(matrix == None):
        matrix = create_single_matrix()
        
    det = determinant(matrix)
    print(f"Matrix: {matrix}")
    print(f"Determinant of Matrix = {det}") 
    
    return det
    
def determinant(matrix):
    size_of_matrix = len(matrix)
    if(size_of_matrix==1):
        return matrix[0][0]
    elif(size_of_matrix==2):
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    
    det = 0
    for col in range(size_of_matrix):
        sub_matrix = []
        for lookup_row_index in range(1, size_of_matrix): #Skip First Row(at index 0)
            new_row = []
            for lookup_column_index in range(size_of_matrix):
                if(lookup_column_index != col): #If column that is lookup not same as column that we are calculating
                    new_row.append(matrix[lookup_row_index][lookup_column_index])
            sub_matrix.append(new_row)
        
        det += ((-1)** col) * matrix[0][col] * determinant(sub_matrix)
    
    return det

def matrix_inverse(matrix = None):
    if(matrix == None):
        matrix = create_single_matrix()
    
    det = determinant(matrix)
    size_of_matrix = len(matrix)
    
    if det == 0:
        print("This Matrix is Singular Matrix")
        return None
    
    #Hard Code for Matrix of size 2
    if size_of_matrix == 2:
        return [[round(matrix[1][1]/det, 2), round(-matrix[0][1]/det, 2)], 
                [round(-matrix[1][0]/det, 2), round(matrix[0][0]/det, 2)]]
    
    cofactor_matrix = [[0] * size_of_matrix for _ in range(size_of_matrix)]
    for row in range(size_of_matrix):
        for col in range(size_of_matrix):
            minor_matrix = []
            for lookup_row_index in range(size_of_matrix):
                if lookup_row_index == row:
                    continue
                new_row = []
                for lookup_col_index in range(size_of_matrix):
                    if lookup_col_index == col:
                        continue
                    new_row.append(matrix[lookup_row_index][lookup_col_index])
                
                minor_matrix.append(new_row)
            
            #Formula used to construct value cofactor value is (-1)^i+j * det(minor_matrix)
            cofactor_matrix[row][col] = (-1) ** (row + col) * determinant(minor_matrix)
    
    #Last step to create inverse matrix is Transpose cofactor matrix then divide each value of matrix by det of original matrix
    inverse_matrix = matrix_transpose(cofactor_matrix)
    for row in range(size_of_matrix):
        for col in range(size_of_matrix):
            inverse_matrix[row][col] = round(inverse_matrix[row][col] / det, 2)

    print(f"Inverse Matrix: {inverse_matrix}")
    return inverse_matrix
        
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

def create_single_matrix():
    sizex = int(input("Maximum Row of Matrix: "))
    sizey = int(input("Maximum Column of Matrix: "))
    
    matrix = [[0] * sizey for _ in range(sizex)]
    
    for row in range(0, sizex):
        for col in range(0, sizey):
            val = int(input(f"Matrix | Enter Value of POsition [{row}][{col}]: "))
            matrix[row][col] = val
    
    return matrix

def get_input_for_matrix_size():   
    sizex_f = int(input("Maximum Row of First Matrix: "))
    sizey_f = int(input("Maximum Column of First Matrix: "))

    sizex_s = int(input("Maximum Row of Second Matrix: "))
    sizey_s = int(input("Maximum Column of Second Matrix: "))
    
    return [sizex_f, sizey_f, sizex_s, sizey_s]
