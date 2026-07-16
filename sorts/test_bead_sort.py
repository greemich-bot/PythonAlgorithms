import unittest
from .bead_sort import bead_sort

'''pytest test_bead_sort.py'''

class TestBeadSort(unittest.TestCase): 
    def test_bead_sort(self): 
        self.assertEqual(bead_sort([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])
    
    def test_bead_sort2(self):
        self.assertEqual(bead_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_bead_sort3(self):
        self.assertEqual(bead_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_bead_sort4(self):
        self.assertEqual(bead_sort([3,3,3]), [3, 3, 3])
    
    def test_bead_sort5(self):
        self.assertEqual(bead_sort([]), [])
    
    def test_bead_sort6(self):
        self.assertEqual(bead_sort([1]), [1])
    
    def test_bead_sort7(self):
        self.assertRaises(TypeError, bead_sort, [2, 1, -2, 1, 2])

    def test_bead_sort8(self):
        self.assertRaises(TypeError, bead_sort, [2, 1, 3.5, 1, 2])