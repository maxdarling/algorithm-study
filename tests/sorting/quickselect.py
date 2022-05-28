from alg.sorting.quickselect import quickselect as qsel
import unittest

class QuickselectTestCase(unittest.TestCase):

    def test_single(self):
        self.assertEqual(qsel([1], 0, 0, 1), 1)

    def test_empty(self):
        self.assertRaises(IndexError, qsel, [], 0, 0, 1)

    def test_basic(self):
        a = [5, 3, 2, 1, 9]
        self.assertEqual(qsel(a, 0, 4, 1), 9)
        self.assertEqual(qsel(a, 0, 4, 2), 5)
        self.assertEqual(qsel(a, 0, 4, 3), 3)
        self.assertEqual(qsel(a, 0, 4, 4), 2)
        self.assertEqual(qsel(a, 0, 4, 5), 1)

    def test_range(self):
        a = [1, 4, 2, 3, 5]
        self.assertEqual(qsel(a, 1, 1, 1), 4)
        self.assertEqual(qsel(a, 2, 3, 2), 2)
        self.assertEqual(qsel(a, 2, 4, 1), 5)
        self.assertEqual(qsel(a, 2, 4, 2), 3)


if __name__ == '__main__':
    unittest.main()

