from matrix_utils import print_matrix

matrix_a = [
    [1, 2],
    [5, 3]
]

matrix_b = [
    [4, 1],
    [7, 5]
]

def subtraction(f_matrix, s_matrix):
    size_f = len(f_matrix)
    size_s = len(s_matrix)
    
    if(size_f != size_s):
        return
    
    r_matrix = [[0] * size_f for _ in range(size_f)]
    
    for m in range(size_f):
        for n in range(size_s):
            r_matrix[m][n] = f_matrix[m][n] - s_matrix[m][n]
            
    print_matrix(r_matrix)
    
subtraction(matrix_a, matrix_b)