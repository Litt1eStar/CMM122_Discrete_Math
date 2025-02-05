from matrix_utils import print_matrix

matrix_a = [
    [-1, 3],
    [4, -2]
]

matrix_b = [
    [4, 3, -2],
    [5, -1, 0]
]

def multiply(matrix_a, matrix_b):
    col_a = len(matrix_a[0])
    row_b = len(matrix_b)
            
    if(col_a != row_b):
        print("Can't Multiply these 2 Matrices")
        return
    
    print(row_b)
    result_matrix = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]
    
    r = 0
    for row in range(len(matrix_a)):
        for col in range(len(matrix_b[0])):
            for k in range(col_a):
                r += matrix_a[row][k] * matrix_b[k][col]
            result_matrix[row][col] = r
            r = 0
    print_matrix(result_matrix)
                
multiply(matrix_a, matrix_b)