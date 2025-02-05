from matrix_utils import print_matrix

matrix_a = [
    [1, 2],
    [5, 3]
]

matrix_b = [
    [4, 1],
    [7, 5]
]

def addition(matrix_a, matrix_b):
    size_f = len(matrix_a)
    size_s = len(matrix_b)
    
    if size_f != size_s:
        return
    
    result_matrix = [[0] * size_f for _ in range(size_f)]
    
    for row in range(size_f):
        for col in range(size_f): 
            result_matrix[row][col] = matrix_a[row][col] + matrix_b[row][col]
        
    print_matrix(result_matrix)
    return

addition(matrix_a, matrix_b)
