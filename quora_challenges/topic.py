import functools

__author__ = 'abhishekanurag'

from location import Location


@functools.total_ordering
class Topic(Location):
    def __init__(self, tid, x, y, source=None):
        Location.__init__(self, x, y, tid)
        if source:
            self.distance = self.dist(source)
        else:
            self.distance = float('inf')  # the max possible

    def __lt__(self, other):
        if other.distance == self.distance:
            return self.lid < other.lid
        else:
            return self.distance > other.distance

    def __eq__(self, other):
        return other.distance == self.distance and self.lid == other.lid

    def __hash__(self):
        return self.lid * self.distance

    def compare_to_topic(self, other):
        if other.distance > self.distance:
            return 1
        elif other.distance == self.distance:
            if self.lid > other.lid:
                return 1
            else:
                return -1
        else:
            return -1

    def __str__(self):
        return self.lid

    def get_topic(self, source):
        return Topic(self.lid, self.x/1000, self.y/1000, source)

