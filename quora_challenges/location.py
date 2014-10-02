import math

__author__ = 'abhishekanurag'

import random


class Location:
    def __init__(self, x, y, lid=None):
        self.x = long(math.ceil(x * 1000))
        self.y = long(math.ceil(y * 1000))
        if lid:
            self.lid = lid
        else:
            self.lid = 0

    def __str__(self):
        return '(' + str(self.lid) + ')' + str(self.x / 1000.0) + ' ' + str(self.y / 1000.0)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @staticmethod
    def compare_x(other1, other2):
        return other1.x <= other2.x

    @staticmethod
    def compare_y(other1, other2):
        return other1.y <= other2.y

    @staticmethod
    def partition_around_median(arr, xy, randomize=True):
        if len(arr) % 2 == 0:
            median = len(arr) / 2 - 1
        else:
            median = len(arr) / 2
        if xy:
            compare = Location.compare_x
        else:
            compare = Location.compare_y
        return Location.kth_smallest(arr, median, compare, randomize)

    @staticmethod
    def kth_smallest(arr, k, compare, randomize=True):
        if k >= len(arr) or k < 0:
            return None
        if randomize:
            pivot_idx = Location.randomized_partition(arr, compare)
        else:
            pivot_idx = Location.partition(arr, compare)
        if pivot_idx == k:
            return arr[k]
        elif pivot_idx < k:
            return Location.kth_smallest(arr[pivot_idx + 1:], k - pivot_idx - 1, compare, randomize)
        else:
            return Location.kth_smallest(arr[:pivot_idx], k, compare, randomize)

    @staticmethod
    def partition(arr, compare):
        i = -1
        if len(arr) > 0:
            i = 0
            part_elem = arr[i]
            for j in range(1, len(arr)):
                if compare(arr[j], part_elem):
                    i += 1
                    Location.swap(arr[i], arr[j])
            Location.swap(arr[0], arr[i])
        return i

    @staticmethod
    def randomized_partition(arr, compare):
        rand = random.randrange(len(arr))
        Location.swap(arr[0],arr[rand])
        return Location.partition(arr, compare)


    @staticmethod
    def swap(l1, l2):
        x = l1.x
        y = l1.y
        lid = l1.lid
        l1.x = l2.x
        l1.y = l2.y
        l1.lid = l2.lid
        l2.x = x
        l2.y = y
        l2.lid = lid

    def dist(self, other):
        x_diff = self.x - other.x
        y_diff = self.y - other.y
        return x_diff * x_diff + y_diff * y_diff
