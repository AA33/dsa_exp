__author__ = 'abhishekanurag'

import Queue


class NearestNeighbors:
    def __init__(self, k, ignore=None):
        self.neighbors = Queue.PriorityQueue(k)
        self.existing_neighbors = set()
        if ignore:
            self.ignore = ignore
        else:
            self.ignore = set()

    def add(self, loc):
        if loc.lid not in self.existing_neighbors and loc.lid not in self.ignore:
            if not self.neighbors.full():
                self.neighbors.put(loc)
                self.existing_neighbors.add(loc.lid)
            else:
                lid = loc.lid
                worst_neighbor = self.peek()
                worst_dist = worst_neighbor.distance
                loc_dist = loc.distance
                better_dist = (worst_dist > loc_dist)
                same_dist_higher_id = (worst_dist == loc_dist and lid > worst_neighbor.lid)
                if better_dist or same_dist_higher_id:
                    self.existing_neighbors.remove(self.neighbors.get().lid)
                    self.neighbors.put(loc)
                    self.existing_neighbors.add(lid)

    def peek(self):
        if self.neighbors.qsize() > 0:
            return self.neighbors.queue[0]
        else:
            return None

    def get_list(self):
        neighbor_list = []
        while not self.neighbors.empty():
            neighbor_list.append(self.neighbors.get())
        return neighbor_list[::-1]

    def is_full(self):
        return self.neighbors.full()
