# Uses python3
import sys
from typing import List, Union, Tuple

def fit_max_of_item(
    spare_capacity: Union[int, float], 
    item_weight: Union[int, float], 
    item_value: Union[int, float]
) -> Tuple[Union[int, float], Union[int, float]]:
    """
    Calculate how much of a specific item we can fit into the spare capacity
    and return the weight and value of that weight of the item.
    """
    if spare_capacity >= item_weight:
        return (item_weight, item_value)
    else:
        return (spare_capacity, item_value/item_weight*spare_capacity)

def get_optimal_value(capacity: int, weights: List[int], values: List[int]):
    value = 0.
    total_weight = 0

    # sort lists by value descending
    VALUE_IDX = 0
    WEIGHT_IDX = 1
    sorted_items = sorted(
        zip(values, weights),
        key=lambda t: t[VALUE_IDX]/t[WEIGHT_IDX],
        reverse=True
    )
    
    item_idx = 0
    while total_weight < capacity and item_idx < len(sorted_items):
        item = sorted_items[item_idx]
        added_weight, added_value = fit_max_of_item(
            spare_capacity=capacity-total_weight,
            item_weight=item[WEIGHT_IDX],
            item_value=item[VALUE_IDX],
        ) 
        total_weight += added_weight
        value += added_value
        item_idx += 1
    return value


from unittest import TestCase

class TestGetChange(TestCase):

    # test corner cases
    def test_simple_case1(self):
        capacity = 50
        weights = [20, 50, 30]
        values = [60, 100, 120]
        self.assertEquals(get_optimal_value(capacity, weights, values), 180.00)
    
    def test_simple_case2(self):
        capacity = 10
        weights = [30]
        values = [500]
        self.assertAlmostEquals(get_optimal_value(capacity, weights, values), 166.6667, places=4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
