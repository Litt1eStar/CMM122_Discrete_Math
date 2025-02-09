import unittest
from function_relation import isFunction, is_surjective_function, is_injective_function, domain_and_range, inverse_relation
class TestFunctionRelationOperation(unittest.TestCase):
    def test_is_function(self):
        relation1 = {(1, 2), (3, 4), (5, 6)}
        relation2 = {(1, 2), (1, 6), (5, 6)}
        expected_result1 = True
        expected_result2 = False
        
        
        result1 = isFunction(relation1)
        self.assertEqual(result1, expected_result1)

        result2 = isFunction(relation2)
        self.assertEqual(result2, expected_result2)
        
    def test_domain_range(self):
        relation = {(1,2), (3, 4)}
        expected_result = [[1, 3], [2, 4]]
        
        result = domain_and_range(relation)
        self.assertEqual(result, expected_result)
        
    def test_is_injective_function(self):
        relation1 = {(1,2), (3, 4)}
        expected_result1 = True
        relation2 = {(1,2), (3, 2)}
        expected_result2 = False
        
        result1 = is_injective_function(relation1)
        self.assertEqual(result1, expected_result1)
        
        result2 = is_injective_function(relation2)
        self.assertEqual(result2, expected_result2)
        
    def test_is_surjective_function(self):
        relation1 = {(1,2), (3, 2)}
        expected_result1 = True
        relation2 = {(1,4), (3, 5)}
        expected_result2 = False
        
        result1 = is_surjective_function(relation1)
        self.assertEqual(result1, expected_result1)
        
        result2 = is_surjective_function(relation2)
        self.assertEqual(result2, expected_result2)
        
    def test_inverse_relation(self):
        relation = {(1, 2), (3, 4)}
        expected_result = {(2, 1), (4, 3)}
        
        result = inverse_relation(relation)
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()