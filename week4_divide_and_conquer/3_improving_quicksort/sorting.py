# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]  # This is the pivot value to partion around.
    j1, j2 = l, l  # These are the indeces at the boundaries of the middle
                   # partition which holds the duplicates of x.
                   # It is used for swaps between the lower and higher parttion
                   # in order to extend the lower partition.
    for i in range(l + 1, r + 1):
        if a[i] == x:
            j2 += 1
            a[i], a[j2] = a[j2], a[i]
        if a[i] < x:
            j1 += 1
            j2 += 1
            a[i], a[j1] = a[j1], a[i]
    a[l], a[j1] = a[j1], a[l]
    return j1, j2

def partition2(a, l, r):
    x = a[l]  # this is the pivot value to partion around
    j = l   # this is the index of the right-most element in the left partition
            # it is used for swaps between the lower and higher parttion in
            # order to extend the lower partition
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort_2_partitions(a, l, r):
    """
    Works well if there are not many duplicates in the input (mostly unique)
    """
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, m + 1, r)


def randomized_quick_sort(a, l, r):
    """
    Uses three partitions in case we have many duplicates. 
    """
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)

from unittest import TestCase


class TestSolution(TestCase):
    
    def test_partitioning(self):
        a = [2, 3, 2, 2, 9]
        partition3(a, 0, len(a) - 1)
        self.assertEqual(
            a[:3], 
            [2, 2, 2]
        )


    def test_simple1(self):
        a = [2, 3, 9, 2, 2]
        n = len(a)
        randomized_quick_sort(a, 0, n - 1)
        self.assertEqual(a, [2, 2, 2, 3, 9])


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
