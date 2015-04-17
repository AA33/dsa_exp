from collections import deque
from collections import defaultdict

__author__ = 'abhishekanurag'

'''
Problem statement: You are given a NxN array of positive integers representing a continent. Each integer represents the height of that square of the continent block.
On the north and west of the continent lies the Atlantic and on the south and east lies the Pacific.
If height of oceans is 0 and rainfall can occur on any block of the continent, return the list of blocks from where water can flow both to the Atlantic and the Pacific.
'''

import unittest


class ContinentalDriftTest(unittest.TestCase):
    def setUp(self):
        pass

    '''
    []
    '''

    def test_drift_base0(self):
        base = [[]]
        two_ways = to_both_oceans(base)
        assert (len(two_ways) == 0)

    '''
    [*5]
    '''

    def test_drift_base1(self):
        base = [[5]]
        two_ways = to_both_oceans(base)
        assert (len(two_ways) == 1)
        assert (two_ways[0] == (0, 0))

    '''
    [*5 *4]
    [*4 *5]
    '''

    def test_drift_base2(self):
        base = [[5, 4], [4, 5]]
        two_ways = to_both_oceans(base)
        assert (len(two_ways) == 4)

    '''
    [3 2 *3]
    [2 *5 2]
    [*3 2 3]
    '''

    def test_drift_small(self):
        small = [[3, 2, 3], [2, 5, 2], [3, 2, 3]]
        two_ways = to_both_oceans(small)
        assert (len(two_ways) == 3)
        assert (two_ways[0] == (0, 2))
        assert (two_ways[1] == (1, 1))
        assert (two_ways[2] == (2, 0))

    '''
    [1, 1, 1, *2,  *2],
    [1, *5, *6, *3, 1],
    [1, *4, *7, *5, 1],
    [1, *3, *6, 4,  1],
    [*2, *2, 1, 1,  1]
    '''

    def test_drift_medium(self):
        medium = [[1, 1, 1, 2, 2],
                  [1, 5, 6, 3, 1],
                  [1, 4, 7, 5, 1],
                  [1, 3, 6, 4, 1],
                  [2, 2, 1, 1, 1]]
        two_ways = to_both_oceans(medium)
        assert (len(two_ways) == 12)


def to_both_oceans(continent):
    graph = get_graph(continent)
    blocks_to_pacific = to_pacific(continent, graph)
    blocks_to_atlantic = to_atlantic(continent, graph)

    to_both = [(i, j) for i in range(len(blocks_to_atlantic)) for j in range(len(blocks_to_atlantic[0]))
               if blocks_to_atlantic[i][j] and blocks_to_pacific[i][j]]
    return to_both


def get_graph(continent):
    graph = defaultdict(list)
    for i in range(len(continent)):
        for j in range(len(continent[0])):
            height = seek_loc(continent, (i, j))
            if i - 1 >= 0 and seek_loc(continent, (i - 1, j)) >= height:
                graph[(i, j)].append((i - 1, j))
            if j - 1 >= 0 and seek_loc(continent, (i, j - 1)) >= height:
                graph[(i, j)].append((i, j - 1))
            if i + 1 < len(continent) and seek_loc(continent, (i + 1, j)) >= height:
                graph[(i, j)].append((i + 1, j))
            if j + 1 < len(continent[0]) and seek_loc(continent, (i, j + 1)) >= height:
                graph[(i, j)].append((i, j + 1))
    return graph


def to_one_ocean(start, graph, size):
    one_ocean = [[False for _ in range(size[0])] for _ in range(size[1])]
    already_set = set()
    while len(start) > 0:
        this_works = start.popleft()
        set_loc(one_ocean, this_works)
        already_set.add(this_works)
        start.extend(set(graph[this_works]) - already_set)
    return one_ocean


def to_pacific(continent, graph):
    pacific = deque()
    # append first column
    for i in range(len(continent)):
        if len(continent[i]) > 0:
            pacific.append((i, 0))
    # append first row
    for i in range(1, len(continent[0])):
        pacific.append((0, i))
    return to_one_ocean(pacific, graph, (len(continent), len(continent[0])))


def to_atlantic(continent, graph):
    atlantic = deque()
    # append last column
    last_col = len(continent[0]) - 1
    if last_col >= 0:
        for i in range(len(continent)):
            atlantic.append((i, last_col))
    # append last row
    last_row = len(continent) - 1
    if last_row >= 0:
        for i in range(len(continent[0]) - 1):
            atlantic.append((last_row, i))
    return to_one_ocean(atlantic, graph, (len(continent), len(continent[0])))


def seek_loc(continent, loc):
    return continent[loc[0]][loc[1]]


def set_loc(to_ocean, loc):
    to_ocean[loc[0]][loc[1]] = True

