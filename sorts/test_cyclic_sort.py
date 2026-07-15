import unittest
from .cyclic_sort import cyclic_sort
import pytest

pytestmark = pytest.mark.timeout(1)   # Set timeout to 1 second

'''
run: pytest test_cyclic_sort.py
'''


class TestCyclicSort(unittest.TestCase):
    def test_cyclic_sort1(self):
        '''
        Test cyclic_sort with an unsorted array of four elements.
        '''
        arr = [4, 3, 1, 2]
        cyclic_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4])

    def test_cyclic_sort2(self):
        """test negatives"""
        arr = [1, 3, -2, 4]
        cyclic_sort(arr)
        self.assertEqual(arr, [-2, 1, 3, 4])

    def test_cyclic_sort3(self):
        """test duplicates"""
        arr = [4, 2, 4, 3, 2]
        cyclic_sort(arr)
        self.assertEqual(arr, [2, 2, 3, 4, 4])

    def test_cyclic_sort4(self):
        """test empty array"""
        arr = []
        cyclic_sort(arr)
        self.assertEqual(arr, [])

    def test_cyclic_sort5(self):
        """test decimals"""
        arr = [0.1, 0.4, 0.05]
        with self.assertRaises(TypeError):
            cyclic_sort(arr)
