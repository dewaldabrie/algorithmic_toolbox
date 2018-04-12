# Uses python3
import sys
import operator 
from typing import Dict, List

# allowed operation to get the minimum 
# sequence from 1 to n
OPERATOR_ARGUMENT_SUCCESSOP_SUCCESSARG = (
	(operator.add, -1, operator.ge, 1, operator.add, -1),
	(operator.mod, 2, operator.__eq__, 0, operator.floordiv, 2),
	(operator.mod, 3, operator.__eq__, 0, operator.floordiv, 3),
)

def optimal_sequence(n: int) -> List[int]:
    
    # Cache containing minimum operations to arrive 
    # at the number equal to the answer's index.
    # Since we're only interested in numbers from 1 to n, 
    # we will not be using the 0th value in this cache 
    min_ops_cache = [None] * (n + 1)
    min_ops_cache[1] = 1  # trivial initial answer

    # The sequence cache will be keyed by the target number
    # and contain as value the list of numbers in the sequence
    # on the way from 1 to n. More than one minimal sequence
    # may exist for a target - and in that case we will just
    # choose an arbitrary one. 
    sequence_cache: Dict[int, List[int]] = {}
    sequence_cache[1] = [1]  # trivial initial answer

    # Populate the cache lookup
    if n > 1:
        for target in range(2, n + 1):
            #import pdb; pdb.set_trace()
            min_ops = n  # worst case answer
            best_reverse_target = target - 1 # worst case answer
            for reverse_test_op, reverse_test_arg, success_test_op, success_test_arg, prev_target_op, prev_target_arg in OPERATOR_ARGUMENT_SUCCESSOP_SUCCESSARG :
                answ = reverse_test_op(target, reverse_test_arg)
                if success_test_op(answ, success_test_arg):
                    # Find target one hope back
                    # The size of the hop depends on the prev target operator
                    reverse_target = prev_target_op(target, prev_target_arg)
                    ops = min_ops_cache[reverse_target] + 1
                    if ops < min_ops:
                        min_ops = ops
                        best_reverse_target = reverse_target
            min_ops_cache[target] = min_ops
            sequence_cache[target] = sequence_cache[best_reverse_target].copy() + [target] 
           

    # Once the cache/lookup is full, lookup the answer
    return sequence_cache[n]


from unittest import TestCase

class TestSolution(TestCase):

    def test_sample_1(self):
        self.assertEqual(
            list(optimal_sequence(1)),
            [1]
        )

    def test_sample_2(self):
        self.assertEqual(
            len(list(optimal_sequence(5))),
            len([1 , 2, 4, 5])
        )

    def test_sample_3(self):
        self.assertEqual(
            len(list(optimal_sequence(96234))),
            len([1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234])
        )

if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
