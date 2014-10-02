from nearby import Question

__author__ = 'abhishekanurag'

from nearby import Location
from nearby import Topic
from nearby import TwoDTree
import unittest

locations = [Location(1, 1), Location(2, 2), Location(3, 3), Location(4, 4), Location(1, 4)]
topics = [Topic(1, 1, 1), Topic(2, 2, 2), Topic(3, 3, 3), Topic(4, 4, 4), Topic(5, 1, 4)]


class LocationTest(unittest.TestCase):
    loc = Location(5.567, 6.98887)

    def test_init(self):
        assert (self.loc.x == 5567)
        assert (self.loc.y == 6989)

    def test_str(self):
        assert (str(self.loc) == '(0)5.567 6.989')

    def test_partition(self):
        assert (Location.partition_around_median(locations, True) == Location(2, 2))
        assert (Location.partition_around_median(locations, False) == Location(3, 3))


class TopicTest(unittest.TestCase):
    topic1 = Topic(5, 1, 1, Topic(2, 2, 2))
    topic2 = Topic(1, 1, 1)
    topic3 = Topic(6, 1, 1, Topic(2, 2, 2))
    topic4 = Topic(4, 1, 1, Topic(2, 2, 2))

    def test_init(self):
        assert (self.topic1.distance == 2000000)
        assert (self.topic2.distance == float('inf'))

    def test_compare(self):
        assert (self.topic1.compare_to_topic(self.topic2) > 0)
        assert (self.topic1.compare_to_topic(self.topic3) < 0)
        assert (self.topic1.compare_to_topic(self.topic4) > 0)


class TreeTest(unittest.TestCase):
    def test_init(self):
        tree = TwoDTree(locations, randomize=False)
        assert (tree.loc == Location(2, 2))
        assert (tree.left.loc == Location(1, 1))
        assert (tree.right.loc == Location(3, 3))

        assert (tree.left.left is None)
        assert (tree.left.right.loc == Location(1, 4))
        assert (tree.right.left is None)
        assert (tree.right.right.loc == Location(4, 4))

    def test_nearest_neighbors(self):
        tree = TwoDTree(topics, randomize=True)

        # Simple test for 1 nearest neighbor
        nns = tree.k_nearest_neighbors(Location(1.5, 1), 1)
        assert (len(nns) == 1)
        assert (nns[0].lid == 1)

        # Same test with max nearest possible
        nns = tree.k_nearest_neighbors(Location(1.5, 1), 6)
        assert (len(nns) == 5)
        assert (nns[0].lid == 1)
        assert (nns[1].lid == 2)
        assert (nns[2].lid == 3)
        assert (nns[3].lid == 5)
        assert (nns[4].lid == 4)

        # Test with existing location in tree
        nns = tree.k_nearest_neighbors(Location(1, 1), 2)
        assert (len(nns) == 2)
        assert (nns[0].lid == 1)
        assert (nns[1].lid == 2)

        #Test with id precedence
        nns = tree.k_nearest_neighbors(Location(2.5, 4), 3)
        assert (len(nns) == 3)
        assert (nns[0].lid == 3)
        assert (nns[1].lid == 5)
        assert (nns[2].lid == 4)

        nns = tree.k_nearest_neighbors(Location(3.5, 3), 3)
        assert (len(nns) == 3)
        assert (nns[0].lid == 3)
        assert (nns[1].lid == 4)
        assert (nns[2].lid == 2)

        nns = tree.k_nearest_neighbors(Location(3.5, 3), 2)
        assert (len(nns) == 2)
        assert (nns[0].lid == 3)
        assert (nns[1].lid == 4)

        nns = tree.k_nearest_neighbors(Location(3.5, 2), 3)
        assert (len(nns) == 3)
        assert (nns[0].lid == 3)
        assert (nns[1].lid == 2)
        assert (nns[2].lid == 4)

        nns = tree.k_nearest_neighbors(Location(1.5, 3), 5)
        assert (len(nns) == 5)
        assert (nns[0].lid == 5)
        assert (nns[1].lid == 2)
        assert (nns[2].lid == 3)
        assert (nns[3].lid == 1)
        assert (nns[4].lid == 4)

        nns = tree.k_nearest_neighbors(Location(2.5, 5), 5)
        assert (len(nns) == 5)
        assert (nns[0].lid == 5)
        assert (nns[1].lid == 4)
        assert (nns[2].lid == 3)
        assert (nns[3].lid == 2)
        assert (nns[4].lid == 1)

        nns = tree.k_nearest_neighbors(Location(2.5, 0), 5)
        assert (len(nns) == 5)
        assert (nns[0].lid == 1)
        assert (nns[1].lid == 2)
        assert (nns[2].lid == 3)
        assert (nns[3].lid == 5)
        assert (nns[4].lid == 4)

        nns = tree.k_nearest_neighbors(Location(0, 2.5), 5)
        assert (len(nns) == 5)
        assert (nns[0].lid == 5)
        assert (nns[1].lid == 1)
        assert (nns[2].lid == 2)
        assert (nns[3].lid == 3)
        assert (nns[4].lid == 4)

        nns = tree.k_nearest_neighbors(Location(5, 2.5), 5)
        assert (len(nns) == 5)
        assert (nns[0].lid == 4)
        assert (nns[1].lid == 3)
        assert (nns[2].lid == 2)
        assert (nns[3].lid == 5)
        assert (nns[4].lid == 1)


class QuestionTest(unittest.TestCase):
    def test_init(self):
        q = Question(23, topics, search=Location(1.5, 1))
        assert (q.current_topic.lid == 1)

        q = Question(24, topics, search=Location(2.5, 2.5))
        assert (q.current_topic.lid == 3)

        q = Question(25, topics)
        q1 = q.get_question(Location(2, 3))
        assert (q1.qid == 25)
        assert (q1.current_topic.lid == 3)


if __name__ == '__main__':
    unittest.main()