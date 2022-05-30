from alg.sorting.rotate import rotate
import unittest
from copy import deepcopy as cpy

class RotateTestCase(unittest.TestCase):

    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3, 4, 5, 6] 

    def test_empty_input(self):
        self.assertEqual(rotate([], 1), [])

    def test_one_element(self):
        self.assertEqual(rotate([1], 2), [1])

    def test_basic_1(self):
        self.assertEqual(rotate(cpy(self.a), 0), [1, 2, 3, 4, 5])
        self.assertEqual(rotate(cpy(self.a), 1), [2, 3, 4, 5, 1])
        self.assertEqual(rotate(cpy(self.a), 2), [3, 4, 5, 1, 2])
        self.assertEqual(rotate(cpy(self.a), 3), [4, 5, 1, 2, 3])
        self.assertEqual(rotate(cpy(self.a), 4), [5, 1, 2, 3, 4])
        self.assertEqual(rotate(cpy(self.a), 5), [1, 2, 3, 4, 5])
        self.assertEqual(rotate(cpy(self.a), 6), [2, 3, 4, 5, 1])

    def test_basic_2(self):
        self.assertEqual(rotate(cpy(self.b), 0), [1, 2, 3, 4, 5, 6])
        self.assertEqual(rotate(cpy(self.b), 1), [2, 3, 4, 5, 6, 1])
        self.assertEqual(rotate(cpy(self.b), 2), [3, 4, 5, 6, 1, 2])
        self.assertEqual(rotate(cpy(self.b), 3), [4, 5, 6, 1, 2, 3])
        self.assertEqual(rotate(cpy(self.b), 4), [5, 6, 1, 2, 3, 4])
        self.assertEqual(rotate(cpy(self.b), 5), [6, 1, 2, 3, 4, 5])
        self.assertEqual(rotate(cpy(self.b), 6), [1, 2, 3, 4, 5, 6])
        self.assertEqual(rotate(cpy(self.b), 7), [2, 3, 4, 5, 6, 1])

    def test_right_rotate_1(self):
        self.assertEqual(rotate(cpy(self.a), -1), [5, 1, 2, 3, 4])
        self.assertEqual(rotate(cpy(self.a), -2), [4, 5, 1, 2, 3])
        self.assertEqual(rotate(cpy(self.a), -3), [3, 4, 5, 1, 2])
        self.assertEqual(rotate(cpy(self.a), -4), [2, 3, 4, 5, 1])
        self.assertEqual(rotate(cpy(self.a), -5), [1, 2, 3, 4, 5])
        self.assertEqual(rotate(cpy(self.a), -6), [5, 1, 2, 3, 4])

    def test_right_rotate_1(self):
        self.assertEqual(rotate(cpy(self.b), -1), [6, 1, 2, 3, 4, 5])
        self.assertEqual(rotate(cpy(self.b), -2), [5, 6, 1, 2, 3, 4])
        self.assertEqual(rotate(cpy(self.b), -3), [4, 5, 6, 1, 2, 3])
        self.assertEqual(rotate(cpy(self.b), -4), [3, 4, 5, 6, 1, 2])
        self.assertEqual(rotate(cpy(self.b), -5), [2, 3, 4, 5, 6, 1])
        self.assertEqual(rotate(cpy(self.b), -6), [1, 2, 3, 4, 5, 6])
        self.assertEqual(rotate(cpy(self.b), -7), [6, 1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()


