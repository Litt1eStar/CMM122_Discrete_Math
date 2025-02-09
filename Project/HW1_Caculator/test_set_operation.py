import unittest
from set_operations import set_union, set_intersection, set_difference, set_complement

class TestSetOperations(unittest.TestCase):
    def test_set_union(self):
        setA = [1, 2, 4]
        setB = [3, 5, 6]
        expected_result = [1, 2, 3, 4, 5, 6]
        
        result = set_union(setA, setB)
        self.assertEqual(result, expected_result)
    
    def test_set_intersection(self):
        setA = [1, 2, 3]
        setB = [1, 2]
        expected_result = [1, 2]
        
        result = set_intersection(setA, setB)
        self.assertEqual(result, expected_result)
        
    def test_set_difference(self):
        setA = [1, 2, 3]
        setB = [2, 3]
        expected_result = [1]
        
        result = set_difference(setA, setB)
        self.assertEqual(result, expected_result)
    
    def test_set_complement(self):
        setA = [1, 2, 3]
        setB = [1, 2, 3, 4, 5]
        expected_result = [4, 5]
        
        result = set_complement(setA, setB)
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()