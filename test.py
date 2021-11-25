#!/usr/bin/python3
# Test case for calculating median of list of numbers

import unittest
from program import median

class TestMean(unittest.TestCase):
    def test1(self):
        data = [1,2,3]
        result = median(data)
        self.assertEqual(result, 2)

    def test2(self):
        data = [1,2,3,4]
        result = median(data)
        self.assertEqual(result, 2.5)

if __name__ == '__main__':
    unittest.main()
