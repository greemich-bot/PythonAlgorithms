import unittest
from .gnome_sort import gnome_sort


class TestGnomeSort(unittest.TestCase):
    def test_gnome_sort1(self):
        arr = [4, 3, 1, 2]
        gnome_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4])

    def test_gnome_sort2(self):
        arr = [1, 3, -2, 4]
        gnome_sort(arr)
        self.assertEqual(arr, [-2, 1, 3, 4])

    def test_gnome_sort3(self):
        arr = [4, 2, 4, 3, 2]
        gnome_sort(arr)
        self.assertEqual(arr, [2, 2, 3, 4, 4])

    def test_gnome_sort4(self):
        arr = []
        gnome_sort(arr)
        self.assertEqual(arr, [])

    def test_gnome_sort5(self):
        arr = [0.1, 0.4, 0.05]
        gnome_sort(arr)
        self.assertEqual(arr, [0.05, 0.1, 0.4])

if __name__ == '__main__':
    unittest.main()