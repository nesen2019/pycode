from unittest import TestCase
from pycode.random00.L0001_两数之和 import Solution


class TestSolution(TestCase):
    def test_two_sum(self):
        c = Solution()
        print(c.twoSum([2, 7, 12, 15], 9))
