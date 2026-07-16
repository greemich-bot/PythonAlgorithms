import unittest
from .shell_sort import shell_sort

''' pytest test_shell_sort.py'''
class TestShellSort(unittest.TestCase):
    def test1(self):
        arr = [5, 3, 8, 4, 2]
        expected = [2, 3, 4, 5, 8]
        shell_sort(arr)
        self.assertEqual(arr, expected)
    
    def test2(self):
        arr = [10, 7, 3, 1, 9]
        expected = [1, 3, 7, 9, 10]
        shell_sort(arr)
        self.assertEqual(arr, expected)
    
    def test3(self):
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        shell_sort(arr)
        self.assertEqual(arr, expected)
    
    def test4(self):
        arr = [-5, 4, 3, 2, 1]
        expected = [-5, 1, 2, 3, 4]
        shell_sort(arr)
        self.assertEqual(arr, expected)

    def test5(self):
        arr = [0, -1, 5, 3, -2]
        expected = [-2, -1, 0, 3, 5]
        shell_sort(arr)
        self.assertEqual(arr, expected)
    
    def test6(self): 
        arr = []
        expected = []
        shell_sort(arr)
        self.assertEqual(arr, expected)
    
    def test7(self):
        arr = [1]
        expected = [1]
        shell_sort(arr)
        self.assertEqual(arr, expected)

    def test8(self):
        arr = [2, 2, 2, 2, 2]
        expected = [2, 2, 2, 2, 2]
        shell_sort(arr)
        self.assertEqual(arr, expected)
    
    def test9(self):
        arr = [1, 3.2, 2.5]
        expected = [1, 2.5, 3.2]
        shell_sort(arr)
        self.assertEqual(arr, expected)
