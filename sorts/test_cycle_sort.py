import unittest
from .cycle_sort import cycle_sort

'''pytest test_cycle_sort.py'''
class TestCycleSort(unittest.TestCase):
    def test_cycle_sort1(self):
        '''
        Test cycle_sort with an unsorted array of four elements.
        '''
        arr = [4, 3, 1, 2]
        cycle_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4])

    def test_cycle_sort2(self):
        '''
        Test cycle_sort with an already sorted array of four elements
        with negatives.
        '''
        arr = [-1, 3, -2, 4]
        cycle_sort(arr)
        self.assertEqual(arr, [-2, -1, 3, 4])

    def test_cycle_sort3(self):
        '''
        Test cycle_sort with an array containing duplicate elements.
        '''
        arr = [4, 2, 4, 3, 2]
        cycle_sort(arr)
        self.assertEqual(arr, [2, 2, 3, 4, 4])

    def test_cycle_sort4(self):
        '''
        Test cycle_sort with an empty array.
        '''
        arr = []
        cycle_sort(arr)
        self.assertEqual(arr, [])

    def test_cycle_sort5(self):
        '''
        Test cycle_sort decimals
        '''
        arr = [.1, .4, .05]
        cycle_sort(arr)
        self.assertEqual(arr, [.05, .1, .4])
    
    def test_cycle_sort6(self):
        '''
        Test cycle_sort with a single-element array.
        '''
        arr = [1]
        cycle_sort(arr)
        self.assertEqual(arr, [1])

    def test_cycle_sort7(self):
        '''
        Test cycle_sort with an empty array.
        '''
        arr = []
        cycle_sort(arr)
        self.assertEqual(arr, [])

if __name__ == '__main__':
    unittest.main()
