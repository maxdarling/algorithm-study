from alg.sorting.partition import partition
import unittest

class PartitionTestCase(unittest.TestCase):

    def test_basic_1(self):
        a = [9, 2, 3, 7, 6, 4, 1, 1, 8]
        self.assertEqual(partition(a, 0, 8, 4), 5)  

    def test_empty_input(self):
        self.assertRaises(IndexError, partition, [], 0, 0, 0)

    def test_one_element(self):
        self.assertEqual(partition([5], 0, 0, 0), 0)

    def test_homogenous(self):
        self.assertEqual(partition([1, 1, 1, 1], 0, 3, 0), 0)

    def test_range_1(self):
        a = [9, 3, 2, 1, 9]
        res = partition(a, 1, 3, 2)
        self.assertEqual(res, 2)
        self.assertEqual(a, [9, 1, 2, 3, 9])

    def test_range_2(self):
        a = [9, 3, 2, 1, 9]
        res = partition(a, 0, 3, 2)
        self.assertEqual(res, 1)
        self.assertEqual(a, [1, 2, 9, 3, 9])

    def test_range_3(self):
        a = [9, 3, 2, 1, 9]
        res = partition(a, 1, 4, 2)
        self.assertEqual(res, 2)
        self.assertEqual(a, [9, 1, 2, 3, 9])


if __name__ == '__main__':
    unittest.main()


