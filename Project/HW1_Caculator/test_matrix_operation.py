import unittest
from matrix_operations import matrix_addition, matrix_subtraction, matrix_determinant, matrix_transpose, matrix_scalar_multiplication, matrix_multiplication, matrix_inverse
class TestMatrixOperations(unittest.TestCase):
    def test_matrix_addition(self):
        matrix_a = [[1, 2], [3, 4]]
        matrix_b = [[5, 6], [7, 8]]
        expected_result = [[6, 8], [10, 12]]
        
        result = matrix_addition(matrix_a, matrix_b)
        self.assertEqual(result, expected_result)
    
    def test_matrix_subtraction(self):
        matrix_a = [[5, 6], [7, 8]]
        matrix_b = [[1, 2], [3, 4]]
        expected_result = [[4, 4], [4, 4]]
        
        result = matrix_subtraction(matrix_a, matrix_b)
        self.assertEqual(result, expected_result)

    def test_matrix_multiplication(self):
        matrix_a = [[1, 2], [3, 4]]
        matrix_b = [[5, 6], [7, 8]]
        expected_result = [[19, 22], [43, 50]]
        
        result = matrix_multiplication(matrix_a, matrix_b)
        self.assertEqual(result, expected_result)
    
    def test_matrix_scalar_multiplication(self):
        matrix_a = [[1, 2], [3, 4]]
        scalar_value = 10
        expected_result = [[10, 20], [30, 40]]
        
        result = matrix_scalar_multiplication(matrix_a, scalar_value)
        self.assertEqual(result, expected_result)
        
    def test_matrix_transpose(self):
        matrix_a = [[1, 2], [3, 4]]
        expected_result = [[1,3], [2,4]]
        
        result = matrix_transpose(matrix_a)
        self.assertEqual(result, expected_result)
if __name__ == '__main__':
    unittest.main()
