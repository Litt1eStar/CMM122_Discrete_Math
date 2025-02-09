import unittest
from vector_operation import vector_addition, vector_subtraction, vector_scalar_multiplication, vector_dot_product, vector_cross_product

class TestVectorOperation(unittest.TestCase):
    def test_vector_addition(self):
        vectors = [[1, 2, 3], [1, 1, 1]]
        expected_result = [2, 3, 4]
        
        result = vector_addition(vectors)
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()    