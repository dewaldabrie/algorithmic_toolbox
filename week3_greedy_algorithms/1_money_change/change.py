# Uses python3
import sys
import random

# possible coin values
# this must be sorted in descending order
DENOMINATIONS = (10, 5, 1)

def get_change(m, denomination_idx=0):
    """
    Compose the target value out of as few denominations as possible
    using only addition.
    """
    total_coins = 0
    quotient, remainder = divmod(m, DENOMINATIONS[denomination_idx])
    total_coins += quotient
    if remainder != 0:
        total_coins += get_change(
            remainder, 
            denomination_idx=min(denomination_idx+1, len(DENOMINATIONS)-1)
        )

    return total_coins


from unittest import TestCase

class TestGetChange(TestCase):

    # test corner cases
    def test_simple_cases(self):
        self.assertEquals(get_change(2), 2)
        self.assertEquals(get_change(28), 6)

    def test_stress(self):
        """
        Compare our fast algo against a naive algo using random imputs
        """
        pass

if __name__ == '__main__':

    m = int(input())
    print(get_change(m))

