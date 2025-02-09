from utils import get_choice, clear_screen
from colorama import Fore, Style
from tabulate import tabulate

def matrix_menu():
    while True:
        clear_screen()
        menu_options = [
            ["1", "Addition"],
            ["2", "Subtraction"],
            ["3", "Multiplication"],
            ["4", "Scalar Multiplication"],
            ["5", "Transpose"],
            ["6", "Determinant"],
            ["7", "Inverse"],
            ["8", "Return to Previous Menu"]
        ]

        print(Fore.GREEN + "\n\tMatrix Operations\n" + Style.RESET_ALL)
        print(tabulate(menu_options, headers=["Option", "Operation"], tablefmt="fancy_grid"))


        choice = get_choice(1, 8)
        if choice == 8:
            break

        if choice == 1:
            result = matrix_addition()
        elif choice == 2:
            result = matrix_subtraction()
        elif choice == 3:
            result = matrix_multiplication()
        elif choice == 4:
            result = matrix_scalar_multiplication()
        elif choice == 5:
            result = matrix_transpose()
        elif choice == 6:
            result = matrix_determinant()
        elif choice == 7:
            result = matrix_inverse()
        
        if result is not None:
            if(type(result) == int):
                print(Fore.CYAN + "\nResult: " + str(result) + Style.RESET_ALL)
            else:
                print(Fore.CYAN + "\nResult:" + Style.RESET_ALL)
                print_matrix(result)

        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
            
def matrix_addition(matrix_a = None, matrix_b = None):
    if(matrix_a == None and matrix_b == None):
        sizes = get_input_for_matrix_size()    
        input_matrix = create_matrix("Addition", sizes[0], sizes[1], sizes[2], sizes[3])
        
        matrix_a = input_matrix[0]
        matrix_b = input_matrix[1]
        
    result_matrix = [[0] * len(matrix_a[0]) for _ in range(len(matrix_a))]
    
    for row in range(len(matrix_a)):
        for col in range(len(matrix_a[0])):
            result_matrix[row][col] = matrix_a[row][col] + matrix_b[row][col]
    
    print(Fore.MAGENTA + "\nMatrix A:" + Style.RESET_ALL)
    print_matrix(matrix_a)
    print(Fore.MAGENTA + "\nMatrix B:" + Style.RESET_ALL)
    print_matrix(matrix_b)
    print(Fore.GREEN + "\nMatrix A + Matrix B:" + Style.RESET_ALL)
    
    return result_matrix
    
def matrix_subtraction(matrix_a = None, matrix_b = None):
    if(matrix_a == None and matrix_b == None):
        sizes = get_input_for_matrix_size()  
        input_matrix = create_matrix("Subtraction", sizes[0], sizes[1], sizes[2], sizes[3])
        
        matrix_a = input_matrix[0]
        matrix_b = input_matrix[1]
    
    result_matrix = [[0] * len(matrix_a[0]) for _ in range(len(matrix_a))]
    
    for row in range(len(matrix_a)):
        for col in range(len(matrix_a[0])):
            result_matrix[row][col] = matrix_a[row][col] - matrix_b[row][col]        

    print(Fore.MAGENTA + "\nMatrix A:" + Style.RESET_ALL)
    print_matrix(matrix_a)
    print(Fore.MAGENTA + "\nMatrix B:" + Style.RESET_ALL)
    print_matrix(matrix_b)
    print(Fore.GREEN + "\nMatrix A - Matrix B:" + Style.RESET_ALL)
    
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
            for k in range(len(matrix_a[0])):
                result_matrix[row][col] += matrix_a[row][k] * matrix_b[k][col]
                
    print(Fore.MAGENTA + "\nMatrix A:" + Style.RESET_ALL)
    print_matrix(matrix_a)
    print(Fore.MAGENTA + "\nMatrix B:" + Style.RESET_ALL)
    print_matrix(matrix_b)
    print(Fore.GREEN + "\nMatrix A X Matrix B:" + Style.RESET_ALL)
    
    return result_matrix
    
def matrix_scalar_multiplication(matrix = None, scalarVal = None):
    if(matrix == None):
        matrix = create_single_matrix()
    
    if(scalarVal == None):
        scalarVal = int(input("Scalar Value : "))
    temp = [row[:] for row in matrix]  
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            matrix[row][col] *= scalarVal
    
    print(Fore.MAGENTA + "Original Matrix:" + Style.RESET_ALL)
    print_matrix(temp)
    return matrix
    
def matrix_transpose(matrix = None):
    if(matrix == None):
        matrix = create_single_matrix()

    result_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            result_matrix[col][row] = matrix[row][col]
    
    print(Fore.MAGENTA + "\nMatrix A:" + Style.RESET_ALL)
    print_matrix(matrix)
    return result_matrix
    
def matrix_determinant(matrix = None):
    if(matrix == None):
        matrix = create_single_matrix()
        
    det = determinant(matrix)
 
    print(Fore.MAGENTA + "\nMatrix A:" + Style.RESET_ALL)
    print_matrix(matrix)
    
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
        print(Fore.MAGENTA + "\nMatrix A:" + Style.RESET_ALL)
        print_matrix(matrix)
        
        matrix = [[round(matrix[1][1]/det, 2), round(-matrix[0][1]/det, 2)], 
                [round(-matrix[1][0]/det, 2), round(matrix[0][0]/det, 2)]]        

        return matrix
    
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

    print(Fore.MAGENTA + "\nMatrix A:" + Style.RESET_ALL)
    print_matrix(matrix)
    return inverse_matrix
        
def create_matrix(op ,sizex_f, sizey_f, sizex_s, sizey_s):
    is_valid = False
    err_msg = ""
    
    if op == "Addition" or op == "Subtraction":
        is_valid = (sizex_f == sizex_s) and (sizey_f == sizey_s)
        err_msg = f"{Fore.RED}These two matrices must have the same dimension for addition or subtraction"
    elif op == "Multiplication":
        is_valid = sizey_f == sizex_s
        err_msg = f"{Fore.RED}These two matrices can't be multiplied"
    
    if not is_valid:
        print(err_msg)
        return

    first_matrix = [[0] * sizey_f for _ in range(sizex_f)]
    second_matrix = [[0] * sizey_s for _ in range(sizex_s)]
    
    print(Fore.CYAN + "\nEnter values for the First Matrix:")
    for row in range(0, sizex_f):
        for col in range(0, sizey_f):
            val = int(input(f"{Fore.GREEN}First Matrix | Enter Value of Position [{row}][{col}]: "))
            first_matrix[row][col] = val
    
    print(Fore.CYAN + "\nEnter values for the Second Matrix:")
    for row in range(0, sizex_s):
        for col in range(0, sizey_s):
            val = int(input(f"{Fore.GREEN}Second Matrix | Enter Value of Position [{row}][{col}]: "))
            second_matrix[row][col] = val
            
    return [first_matrix, second_matrix]            

def create_single_matrix():
    print(Fore.CYAN + "\nEnter Size of Matrix")
    sizex = int(input(f"{Fore.GREEN}Maximum Row of Matrix: "))
    sizey = int(input(f"{Fore.GREEN}Maximum Column of Matrix: "))
    
    matrix = [[0] * sizey for _ in range(sizex)]
    
    print(Fore.CYAN + "\nEnter Value of Matrix")
    for row in range(0, sizex):
        for col in range(0, sizey):
            val = int(input(f"{Fore.GREEN}Matrix | Enter Value of POsition [{row}][{col}]: "))
            matrix[row][col] = val
    
    return matrix

def get_input_for_matrix_size():   
    print(Fore.CYAN + "\nEnter Matrix Dimensions" + Style.RESET_ALL)
    
    def get_dimension(message):
        while True:
            try:
                value = int(input(Fore.YELLOW + message + Style.RESET_ALL))
                if value > 0:
                    return value
                else:
                    print(Fore.RED + "Error: Please enter a positive integer." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Error: Invalid input. Please enter an integer." + Style.RESET_ALL)

    sizex_f = get_dimension("Enter number of rows for First Matrix: ")
    sizey_f = get_dimension("Enter number of columns for First Matrix: ")
    sizex_s = get_dimension("Enter number of rows for Second Matrix: ")
    sizey_s = get_dimension("Enter number of columns for Second Matrix: ")

    print(Fore.GREEN + "\nMatrix dimensions recorded successfully!\n" + Style.RESET_ALL)

    return [sizex_f, sizey_f, sizex_s, sizey_s]

def print_matrix(matrix):
    formatted_matrix = tabulate(matrix, tablefmt="fancy_grid")
    print(formatted_matrix)
