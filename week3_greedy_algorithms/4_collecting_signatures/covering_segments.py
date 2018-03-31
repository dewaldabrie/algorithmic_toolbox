# Uses python3
import sys
from collections import namedtuple
from typing import List

Segment = namedtuple('Segment', 'start end')

def is_covered(segment: Segment, points: List[int]):
    covered = False
    for point in points:
        if segment.start <= point <= segment.end:
            return True
    return covered

def place_point_at_segement_end(segment: Segment, points: List[int]):
    points.append(segment.end)

def optimal_points(segments):
    points = []
    # safe move is to place a point at the end of each segment if
    # it isn't covered yet.
    # *--------*
    #       *---------*
    #                    *-------------*
    #                                         *------------*
    #                                                      *--------*
    #   *----* *----*
    #          *-----*
    #        
    #         #                        #                   #
    for s in sorted(segments, key=lambda t: t[1]):
        if not is_covered(s, points):
            place_point_at_segement_end(s, points)
            
    return points


from unittest import TestCase

class TestSolution(TestCase):

    def test_simple_1(self):
        segments = [
            Segment(1, 3),
            Segment(2, 5),
            Segment(3, 6),
        ]
        self.assertEquals(optimal_points(segments), [3])

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
