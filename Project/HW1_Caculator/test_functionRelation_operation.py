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
if __name__ == '__main__':
    unittest.main()