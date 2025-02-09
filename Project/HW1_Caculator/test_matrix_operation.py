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


if __name__ == '__main__':
    unittest.main()
