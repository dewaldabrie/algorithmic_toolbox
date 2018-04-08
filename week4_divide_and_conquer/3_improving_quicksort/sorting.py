# Uses python3
import sys
import random
import pdb

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
        elif a[i] < x:
	    # swop first gt element with last eq element
            j2 += 1
            a[i], a[j2] = a[j2], a[i]
            # swop first eq element with with last eq element
            j1 += 1
            a[j2], a[j1] = a[j1], a[j2]

    a[l], a[j1] = a[j1], a[l]
    return j1+1, j2

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
    randomized_quick_sort_2_partitions(a, l, m - 1)
    randomized_quick_sort_2_partitions(a, m + 1, r)

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
    if m1 > l:
        randomized_quick_sort(a, l, m1 - 1)
    if m2 < r - 1:
        randomized_quick_sort(a, m2 + 1, r)

from unittest import TestCase, skip


class TestPartitioning(TestCase):
    
    def test_partitioning(self):
        a = [2, 3, 2, 2, 9]
        partition3(a, 0, len(a) - 1)
        self.assertEqual(
            a[:3], 
            [2, 2, 2]
        )
    
    def test_partitioning2(self):
        a = [2, 2, 2, 2, 9]
        partition3(a, 0, len(a) - 1)
        self.assertEqual(
            a, 
            [2, 2, 2, 2, 9]
        )
    
    def test_partitioning3(self):
        a = [2, 2, 1, 2, 9]
        partition3(a, 0, len(a) - 1)
        self.assertEqual(
            a, 
            [1, 2, 2, 2, 9]
        )

    def test_partitioning4(self):
        a = [9, 9, 2, 9, 1, 2, 9]
        partition3(a, 0, len(a) - 1)
        self.assertEqual(
            a[-4:],
            [9, 9, 9, 9]
        )
    
    def test_partitioning5(self):
        a = [0, 1, 2, 1]
        m1, m2 = partition3(a, 0, len(a) - 1)
        self.assertEqual(
            a[0],
            0
        )

    def test_partitioning6(self):
        a = [1, 0, 2, 1]
        m1, m2 = partition3(a, 0, len(a) - 1)
        self.assertEqual(
            a,
            [0, 1, 1, 2]
        )

    def test_partitioning7(self):
        a = [1, 1, 2, 0]
        m1, m2 = partition3(a, 0, len(a) - 1)
        self.assertEqual(
            a,
            [0, 1, 1, 2]
        )

class TestSorting(TestCase):

    def test_sort1(self):
        a = [2, 3, 9, 2, 2]
        n = len(a)
        randomized_quick_sort(a, 0, n - 1)
        self.assertEqual(a, [2, 2, 2, 3, 9])

    def test_sort2(self):
        a = [2, 3, 9, 2, 2, 9, 9]
        n = len(a)
        randomized_quick_sort(a, 0, n - 1)
        self.assertEqual(a, [2, 2, 2, 3, 9, 9, 9])
    
    def test_sort3(self):
        a = [2, 3, 2, 9, 2, 2, 2]
        n = len(a)
        randomized_quick_sort(a, 0, n - 1)
        self.assertEqual(a, [2, 2, 2, 2, 2, 3, 9])


#@skip("While debugging others")
class TestStress(TestCase):
    
    def test_stress(self):
        while True:
        #for repeat in range(1000):
            #l = random.randint(20, 30)
            l = 4
            a = [random.randint(0, 2) for i in range(l)]
            n = len(a)
            b = [x for x in a]
            randomized_quick_sort(a, 0, n-1),
            randomized_quick_sort_2_partitions(b, 0, n-1),
            self.assertEqual(
                a,
                b,
                msg="3 Partitions yielded %s" % a
            )


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
