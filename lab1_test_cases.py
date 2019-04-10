import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([]), None)
        self.assertEqual(max_list_iter([1, 2, 3, 4, 5, 6, 7]), 7)
        self.assertEqual(max_list_iter([1]), 1)

    def test_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([1]), [1])
        self.assertEqual(reverse_rec([1, 2, 3, 5, 6, 7, 8, 9]), [9, 8, 7, 6, 5, 3, 2, 1])

    def test_bin_search(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(1,1,1,tlist)
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4)
        self.assertEqual(bin_search(5, 1, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 4)
        self.assertEqual(bin_search(5, 1, 8, [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]), 4)
        self.assertEqual(bin_search(5, 1, 9, [5, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 4)
        self.assertEqual(bin_search(5, 1, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 4)
        self.assertEqual(bin_search(5, 1, 9, [1, 5, 3, 4, 3, 6, 7, 8, 9, 10]), 1)
        self.assertEqual(bin_search(0, 1, 9, [1, 5, 3, 4, 3, 6, 7, 8, 9, 10]), None)


if __name__ == "__main__":
    unittest.main()
