import unittest
from .shrink_shell_sort import shell_sort

'''pytest test_shrink_shell_sort.py'''
class TestShrinkShellSort(unittest.TestCase):
    def test1(self):
        arr = [5, 3, 8, 4, 2]
        expected = [2, 3, 4, 5, 8]
        result=shell_sort(arr)
        self.assertEqual(result, expected)
    
    def test2(self):
        arr = [10, 7, 3, 1, 9]
        expected = [1, 3, 7, 9, 10]
        result=shell_sort(arr)
        self.assertEqual(result, expected)

    def test3(self):
        arr = [1, -2, 3, 4, 5]
        expected = [-2, 1, 3, 4, 5]
        result=shell_sort(arr)
        self.assertEqual(result, expected)
    
    def test4(self):
        arr = []
        expected = []
        result=shell_sort(arr)
        self.assertEqual(result, expected)
    
    def test5(self):
        arr = [5]
        expected = [5]
        result=shell_sort(arr)
        self.assertEqual(result, expected)
    
    def test6(self):
        arr = [3, 3, 3]
        expected = [3, 3, 3]
        result=shell_sort(arr)
        self.assertEqual(result, expected)
    
    def test7(self):
        arr = [5, 4.4, 3, 2.9, 1]
        expected = [1, 2.9, 3, 4.4, 5]
        result=shell_sort(arr)
        self.assertEqual(result, expected)