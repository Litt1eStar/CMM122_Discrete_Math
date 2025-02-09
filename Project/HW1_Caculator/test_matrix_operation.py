import unittest
from matrix_operations import matrix_addition
class TestMatrixOperations(unittest.TestCase):
    def test_matrix_addition(self):
        matrix_a = [[1, 2], [3, 4]]
        matrix_b = [[5, 6], [7, 8]]
        expected_result = [[6, 8], [10, 12]]
        
        # Simulating the matrix_addition() function output
        result = matrix_addition(matrix_a, matrix_b)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
