# Uses python3
import sys

DENOMINATIONS = (1, 3, 4)

def get_change(target: int):
    """
    Return the minimal amount of denominations required to sum to the target.
    """ 
    change_cache = [None]*(target + 1)
    change_cache[0] = 0  # trivial answer
    # populate the cache
    min_denom = min(DENOMINATIONS)
    for cache_target in range(1, target+1):
        min_coins = cache_target // min_denom
        for d in DENOMINATIONS:
            one_denom_back = cache_target - d
            if one_denom_back >= 0:
                n_coins_required = change_cache[one_denom_back] + 1
                if n_coins_required < min_coins:
                    min_coins = n_coins_required
        change_cache[cache_target] = min_coins
    
    # as soon as the cache is filled,
    # lookup the correct answer
    return change_cache[target]


from unittest import TestCase

class TestSolution(TestCase):

    def test_sample_1(self):
        self.assertEqual(
            get_change(34),
            9 
        )
        
    def test_sample_2(self):
        self.assertEqual(
            get_change(2),
            2
        )
    
    def test_sample_3(self):
        self.assertEqual(
            get_change(4),
            1
        )


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
