__author__ = 'abhishekanurag'

from indexing import JAVA_KEYWORDS
from indexing.name_trie import NameTrieNode
from indexing.query_processor import QueryProcessor

import unittest
import csv

'''
Unit tests for testing the indexing functionality.
Divided into a small test case and a medium sized test case.
'''


class IndexingTestsSmall(unittest.TestCase):
    def setUp(self):
        self.init_file_name = 'names.csv'
        self.words = [('f', 2), ('fir', 3), ('ho', 4), ('hi', 5), ('f_g', 6), ('go_go', 7)]
        with open(self.init_file_name, 'wb') as names_csv:
            name_writer = csv.writer(names_csv)
            for tuple in self.words:
                name_writer.writerow(list(tuple))
        self.trie = NameTrieNode.construct(self.init_file_name)
        self.qprocessor = QueryProcessor(self.trie)


    def test_query(self):
        result = self.qprocessor.process('f')
        assert (len(result) == 3)
        assert (result[0][1] == 'f_g')
        assert (result[1][1] == 'fir')
        assert (result[2][1] == 'f')

    def test_query2(self):
        result = self.qprocessor.process('g')
        assert (len(result) == 2)
        assert (result[0][1] == 'go_go')
        assert (result[1][1] == 'f_g')


    def test_serialization_and_deserialization(self):
        self.serialized_string = self.trie.serialize()
        deserialized_trie = NameTrieNode.deserialize(self.serialized_string)
        self.qprocessor = QueryProcessor(deserialized_trie)
        self.test_queries()
        self.test_query2()


class IndexingTestsMedium(unittest.TestCase):
    def setUp(self):
        self.init_file_name = 'names2.csv'
        words = []
        for word1 in JAVA_KEYWORDS:
            for word2 in JAVA_KEYWORDS:
                words.append(word1 + '_' + word2)
                words.append(word1 + '_' + word2 + word1)
            words.append('__' + word1)
        self.words = [(w, index) for index, w in enumerate(words)]
        with open(self.init_file_name, 'wb') as names_csv:
            name_writer = csv.writer(names_csv)
            for tuple in self.words:
                name_writer.writerow(list(tuple))
        self.trie = NameTrieNode.construct(self.init_file_name, True)
        self.qprocessor = QueryProcessor(self.trie)


    def test_query(self):
        result = self.qprocessor.process('abstract')
        assert (len(result) == 10)
        assert (result[0][1] == 'while_abstractwhile')
        assert (result[1][1] == 'while_abstract')
        assert (result[2][1] == 'volatile_abstractvolatile')
        assert (result[3][1] == 'volatile_abstract')

    def test_query2(self):
        result = self.qprocessor.process('this')
        assert (len(result) == 10)
        assert (result[0][1] == 'while_thiswhile')
        assert (result[1][1] == 'while_this')
        assert (result[2][1] == 'volatile_thisvolatile')
        assert (result[3][1] == 'volatile_this')


    def test_serialization_and_deserialization(self):
        self.serialized_string = self.trie.serialize()
        deserialized_trie = NameTrieNode.deserialize(self.serialized_string)
        self.qprocessor = QueryProcessor(deserialized_trie)
        self.test_queries()
        self.test_query2()