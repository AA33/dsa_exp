__author__ = 'abhishekanurag'

import math
import random
import functools
import Queue
import sys


class Location:
    def __init__(self, x1, y1, lid=None):
        self.x = long(math.ceil(x1 * 1000))
        self.y = long(math.ceil(y1 * 1000))
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
        part_index = -1
        if len(arr) > 0:
            part_index = 0
            part_elem = arr[part_index]
            for idx in range(1, len(arr)):
                if compare(arr[idx], part_elem):
                    part_index += 1
                    Location.swap(arr[part_index], arr[idx])
            Location.swap(arr[0], arr[part_index])
        return part_index

    @staticmethod
    def randomized_partition(arr, compare):
        rand = random.randrange(len(arr))
        Location.swap(arr[0], arr[rand])
        return Location.partition(arr, compare)

    @staticmethod
    def swap(l1, l2):
        x_coord = l1.x
        y_coord = l1.y
        lid = l1.lid
        l1.x = l2.x
        l1.y = l2.y
        l1.lid = l2.lid
        l2.x = x_coord
        l2.y = y_coord
        l2.lid = lid

    def dist(self, other):
        x_diff = self.x - other.x
        y_diff = self.y - other.y
        return x_diff * x_diff + y_diff * y_diff


@functools.total_ordering
class Topic(Location):
    def __init__(self, topic_id, x1, y1, source=None):
        Location.__init__(self, x1, y1, topic_id)
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
        return Topic(self.lid, self.x / 1000, self.y / 1000, source)


class NearestNeighbors:
    def __init__(self, k, ignore=None):
        self.neighbors = Queue.PriorityQueue(k)
        self.existing_neighbors = set()
        if ignore:
            self.ignore = ignore
        else:
            self.ignore = set()

    def add(self, new_loc):
        if new_loc.lid not in self.existing_neighbors and new_loc.lid not in self.ignore:
            if not self.neighbors.full():
                self.neighbors.put(new_loc)
                self.existing_neighbors.add(new_loc.lid)
            else:
                lid = new_loc.lid
                worst_neighbor = self.peek()
                worst_dist = worst_neighbor.distance
                loc_dist = new_loc.distance
                better_dist = (worst_dist > loc_dist)
                same_dist_higher_id = (worst_dist == loc_dist and lid > worst_neighbor.lid)
                if better_dist or same_dist_higher_id:
                    self.existing_neighbors.remove(self.neighbors.get().lid)
                    self.neighbors.put(new_loc)
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


class TwoDTree:
    def __init__(self, locations, xy=None, randomize=True):
        self.size = len(locations)
        if xy is not None:
            self.xy = xy
        else:
            self.xy = True
        start = 0
        end = self.size - 1
        if self.size % 2 == 0:
            median = self.size / 2 - 1
        else:
            median = self.size / 2
        if start < end:
            self.loc = Location.partition_around_median(locations, self.xy, randomize)
            if start < median:
                self.left = TwoDTree(locations[:median], not self.xy, randomize)
            else:
                self.left = None
            if median < end:
                self.right = TwoDTree(locations[median + 1:], not self.xy, randomize)
            else:
                self.right = None
        elif start == end:
            self.loc = locations[start]
            self.left = self.right = None
        else:
            self.loc = self.left = self.right = None

    def __str__(self):
        return self._to_string('')

    def _to_string(self, prefix):
        if self.xy:
            axis = 'X'
        else:
            axis = 'Y'
        left_str = right_str = ''
        if self.loc:
            self_str = prefix + '{' + str(self.loc) + '(' + str(self.loc.lid) + ')' + '}' + str(self.size)
        else:
            self_str = '{}0'

        if self.left and self.right:
            left_str = '\n|\n' + self.left._to_string(prefix + '---L ' + axis)
            right_str = '\n|\n' + self.right._to_string(prefix + '---R ' + axis)
        elif self.left:
            left_str = '\n|\n' + self.left._to_string(prefix + '---L ' + axis)
        elif self.right:
            right_str = '\n|\n' + self.right._to_string(prefix + '---R ' + axis)

        return self_str + left_str + right_str

    def k_nearest_neighbors(self, search, k, ignore=None):
        if self.size < k:
            search_size = self.size
        else:
            search_size = k
        if ignore:
            nn = NearestNeighbors(search_size, set(ignore))
        else:
            nn = NearestNeighbors(search_size)
        self._knn(nn, search)
        return nn.get_list()

    def _knn(self, nn, search):
        nn.add(self.loc.get_topic(search))

        left_or_right = False  # False = right
        x_axis_and_less = self.xy and search.x <= self.loc.x
        y_axis_and_less = not self.xy and search.y <= self.loc.y
        if x_axis_and_less or y_axis_and_less:
            left_or_right = True  # True = left

        self._get_k_best_from(left_or_right, search, nn)

        if not nn.is_full():
            self._get_k_best_from(not left_or_right, search, nn)
        else:
            current_worst = nn.peek()
            if current_worst:
                x_diff = y_diff = 0
                if self.xy:
                    x_diff = search.x - self.loc.x
                    x_diff = x_diff * x_diff
                else:
                    y_diff = search.y - self.loc.y
                    y_diff = y_diff * y_diff
                worst_dist = current_worst.distance

                x_axis_and_better_dist = self.xy and x_diff <= worst_dist
                y_axis_and_better_dist = not self.xy and y_diff <= worst_dist

                if x_axis_and_better_dist or y_axis_and_better_dist:
                    self._get_k_best_from(not left_or_right, search, nn)

    def _get_k_best_from(self, left_or_right, search, nn):
        if left_or_right and self.left:
            self.left._knn(nn, search)
        elif not left_or_right and self.right:
            self.right._knn(nn, search)


class Question:
    def __init__(self, question_id, assoc_topics=None, topic_tree=None, search=None):
        self.qid = question_id
        if assoc_topics:
            self.topic_tree = TwoDTree(assoc_topics, True, True)
        else:
            self.topic_tree = topic_tree
        if search:
            if self.topic_tree:
                self.current_topic = self.topic_tree.k_nearest_neighbors(search, 1)[0]
            else:
                self.current_topic = None
        else:
            self.current_topic = None

    def __hash__(self):
        return self.qid

    def __eq__(self, other):
        return self.qid == other.qid

    def get_question(self, search):
        return Question(self.qid, topic_tree=self.topic_tree, search=search)


if __name__ == '__main__':
    data = sys.stdin.readline()
    counts = data.split(' ')

    topic_count = int(counts[0])
    question_count = int(counts[1])
    query_count = int(counts[2])

    topics = []
    topic_map = {}
    for i in range(topic_count):
        topic_data = sys.stdin.readline().split(' ')
        tid = int(topic_data[0])
        x = float(topic_data[1])
        y = float(topic_data[2])
        new_topic = Topic(tid, x, y)
        topics.append(new_topic)
        topic_map[tid] = new_topic

    all_topics_tree = TwoDTree(topics)

    question_map = {}
    for i in range(question_count):
        question_data = sys.stdin.readline().split(' ')
        qid = int(question_data[0])
        assoc_topic_count = int(question_data[1])
        assoc_topics = []
        for j in range(2, assoc_topic_count + 2):
            tid = int(question_data[j])
            assoc_topics.append(topic_map[tid])
        if len(assoc_topics) > 0:
            question_map[qid] = Question(qid, assoc_topics)

    for i in range(query_count):
        query_data = sys.stdin.readline().split(' ')
        query_type = query_data[0]
        result_count = int(query_data[1])
        x = float(query_data[2])
        y = float(query_data[3])
        loc = Location(x, y)
        output = ''
        if query_type == 't':
            knn = all_topics_tree.k_nearest_neighbors(loc, result_count)
            for t in knn:
                output += (str(t.lid) + ' ')
        else:
            current_query_topics = []
            topic_to_questions_map = {}
            for qid, question in question_map.iteritems():
                q = question.get_question(loc)
                question_map[qid] = q
                topic = q.current_topic
                if topic:
                    current_query_topics.append(topic)
                    if topic.lid in topic_to_questions_map:
                        topic_to_questions_map[topic.lid].append(qid)
                    else:
                        topic_to_questions_map[topic.lid] = [qid]
            current_topics_tree = TwoDTree(current_query_topics)
            closest_questions = []
            knn_topics = []
            rev_sorted_check = {}

            knn_topics = current_topics_tree.k_nearest_neighbors(loc, result_count)
            results_found = 0
            for topic in knn_topics:
                questions = topic_to_questions_map[topic.lid]
                if topic.lid not in rev_sorted_check:
                    rev_sorted_q = reversed(sorted(questions))
                    topic_to_questions_map[topic.lid] = rev_sorted_q
                    rev_sorted_check[topic.lid] = True
                else:
                    rev_sorted_q = questions
                for question in rev_sorted_q:
                    closest_questions.append(question)
                    results_found += 1
                    if results_found == result_count:
                        break
            for q in closest_questions:
                output += (str(q) + ' ')

        print output[:-1]
