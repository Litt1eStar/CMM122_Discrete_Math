import unittest
from vector_operation import vector_addition, vector_subtraction, vector_scalar_multiplication, vector_dot_product, vector_cross_product

class TestVectorOperation(unittest.TestCase):
    def test_vector_addition(self):
        vectors = [[1, 2, 3], [1, 1, 1]]
        expected_result = [2, 3, 4]
        
        result = vector_addition(vectors)
        self.assertEqual(result, expected_result)
        
    def test_vector_subtraction(self):
        vectors = [[1, 2, 3], [1, 1, 1]]
        expected_result = [0, 1, 2]
        
        result = vector_subtraction(vectors)
        self.assertEqual(result, expected_result)
        
    def test_vector_scalar_multiplication(self):
        vectors = [1, 2, 3]
        scalar_value = 2
        expected_result = [2, 4, 6]
        
        result = vector_scalar_multiplication(vectors, scalar_value)
        self.assertEqual(result, expected_result)
        
    def test_vector_dot_product(self):
        vectors = [[1, 2, 3], [4, 5, 6]]
        expected_result = 32
        
        result = vector_dot_product(vectors)
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()    