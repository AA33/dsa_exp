import sys
from location import Location
from question import Question
from topic import Topic
from twoDTree import TwoDTree

__author__ = 'abhishekanurag'

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




