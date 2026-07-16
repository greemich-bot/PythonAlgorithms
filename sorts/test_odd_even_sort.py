import unittest
from .odd_even_sort import odd_even_sort

'''pytest test_odd_even_sort.py'''


class TestOddEvenSort(unittest.TestCase):
    def test_odd_even_sort1(self):
        arr = [4, 3, 1, 2]
        odd_even_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4])

    def test_odd_even_sort2(self):
        arr = [1, 3, -2, 4]
        odd_even_sort(arr)
        self.assertEqual(arr, [-2, 1, 3, 4])

    def test_odd_even_sort3(self):
        arr = [4, 2, 4, 3, 2]
        odd_even_sort(arr)
        self.assertEqual(arr, [2, 2, 3, 4, 4])

    def test_odd_even_sort4(self):
        arr = []
        odd_even_sort(arr)
        self.assertEqual(arr, [])

    def test_odd_even_sort5(self):
        arr = [0.1, 0.4, 0.05]
        with self.assertRaises(TypeError):
            odd_even_sort(arr)
            
    def test_odd_even_sort6(self):
        arr = [1]
        odd_even_sort(arr)
        self.assertEqual(arr, [1])
    
    