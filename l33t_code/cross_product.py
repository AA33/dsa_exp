import sys

__author__ = 'abhishekanurag'

'''
Given N lists of different sizes produce N-tuple cross product of them
'''


def cross_product(lists):
    sizes = []
    for some_list in lists:
        size = len(some_list)
        if size == 0:
            return []
        sizes.append(size)
    counters = [0] * len(lists)
    product = []
    while counters is not None:
        tuple_list = [lists[i][counters[i]] for i in range(len(counters))]
        product.append(tuple(tuple_list))
        counters = get_next(counters, sizes)
    return product


def get_next(counters, sizes):
    last_index_that_can_be_incremented = -1
    for i in range(len(counters) - 1, -1, -1):
        if counters[i] < sizes[i] - 1:
            last_index_that_can_be_incremented = i
            break
    if last_index_that_can_be_incremented == -1:
        return None
    counters[last_index_that_can_be_incremented] += 1
    for i in range(last_index_that_can_be_incremented + 1, len(counters)):
        counters[i] = 0
    return counters


def main():
    lists = [[1, 2, 3],
             [4, 5],
             [6, 7],
             [8]]
    print cross_product(lists)


if __name__ == '__main__':
    sys.exit(main())