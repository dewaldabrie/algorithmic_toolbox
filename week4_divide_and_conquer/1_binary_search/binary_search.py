# Uses python3
import sys
from random import random, shuffle, randint

def binary_search(a, x):
    """
    Avoid recursion to save stack space.
    """
    left, right = 0, len(a)
    while left < right:
        # compare to middle element
        m = (right+left)//2
        if a[m] == x:
            return m
        elif a[m] < x:  # target is in upper half
            left = m + 1
        else:  # target is in lower half
            right = m
    return -1
    
def linear_search(a, x):
    """
    Naive algo used for stress testing.
    """
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

from unittest import TestCase

class TestSolution(TestCase):
    
    def _test_many(self, func, a, x_list, expected_result_list):
        for target, expected_index in zip(x_list, expected_result_list):
            self.assertEqual(
                func(a, target), 
                expected_index, 
                msg="Func %s failed the test while looking for %d in %s" % (
                    str(func),
                    target, 
                    a
                )
            )

    def test_from_courseware_testcase1(self):
        a = [1, 5, 8, 12, 13]
        x_list = [8, 1, 23, 1, 11]
        expected_result_list = [2, 0, -1, 0, -1]
        self._test_many(linear_search, a, x_list, expected_result_list)
        self._test_many(binary_search, a, x_list, expected_result_list)
    
    def test_binary_search_from_courseware_testcase1(self):
        #    0  1  2  3  4  5  6  7  8   9
        a = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        x_list =               [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        expected_result_list = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
        self._test_many(linear_search, a, x_list, expected_result_list)
        self._test_many(binary_search, a, x_list, expected_result_list)

    def test_under_stress(self):
        for repeat in range(100):
            len = randint(0, 10)
            # unsorted input list
            a = [randint(0, 10e4) for i in range(len)]
            for t in a:
                self.assertEqual(
                    linear_search(a, t),
                    linear_search(a, t),
                )     
        
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end = ' ')
