matrix_a = [
    [1, 2],
    [5, 3]
]

matrix_b = [
    [4, 1],
    [7, 5]
]

def addition(f_matrix, s_matrix):
    size_f = len(f_matrix)
    size_s = len(s_matrix)
    
    if size_f != size_s:
        return
    
    r_matrix = [[0] * size_f for _ in range(size_f)]
    
    for m in range(size_f):
        for n in range(size_f): 
            r_matrix[m][n] = f_matrix[m][n] + s_matrix[m][n]
        
    print_matrix(r_matrix)
    return

def print_matrix(matrix):
    for m in range(len(matrix)):
        for j in range(len(matrix[m])):
            print(matrix[m][j], end=" ")
        print()

addition(matrix_a, matrix_b)
