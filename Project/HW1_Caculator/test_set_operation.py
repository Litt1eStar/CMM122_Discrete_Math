import unittest
from set_operations import set_union, set_intersection, set_difference, set_complement

class TestSetOperations(unittest.TestCase):
    def test_set_union(self):
        setA = [1, 2, 4]
        setB = [3, 5, 6]
        expected_result = [1, 2, 3, 4, 5, 6]
        
        result = set_union(setA, setB)
        self.assertEqual(result, expected_result)
    

if __name__ == '__main__':
    unittest.main()