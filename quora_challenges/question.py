__author__ = 'abhishekanurag'
from twoDTree import TwoDTree


class Question:
    def __init__(self, qid, topics=None, topic_tree=None, search=None):
        self.qid = qid
        if topics:
            self.topic_tree = TwoDTree(topics, True, True)
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

