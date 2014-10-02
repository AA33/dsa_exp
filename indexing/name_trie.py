__author__ = 'abhishekanurag'

import csv
from heapq import heappush, heappushpop
from indexing import is_valid_java_identifier

'''
This module has the key data structure used for indexing - NameTrie
Every non-leaf node of the NameTrie has:
     -A dictionary to maintain its children
     -A min heap to stores the 10 best results for the prefix leading up to the node.
        -- This leads to a lot of wasted space and can be improved.
     -The root node additionally has a set of references to the its child nodes with an _ root, to make the _s searches
     faster
        -- The _s searches are done in parallel by creating subprocesses doing a read only search. More details in
        QueryProcessor
'''


class NameTrieNode:
    MAX_RESULT_SIZE = 10
    END_CHAR = '#'

    def __init__(self, char=None):
        if char:
            self.char = char
        else:
            self.char = '?'
        self.children = {}
        self.num_of_children = 0
        self.best_children = []
        if self.char == '?':
            self.underscore_children = set()

    def __eq__(self, other):
        return id(self) == id(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __str__(self):
        best_children = []
        for child in self.best_children:
            child_string = ','.join([str(child[0]), child[1]])
            best_children.append(child_string)
        best_children_string = '|'.join(best_children)
        string_rep = [self.char, best_children_string, str(len(self.children))]
        return ' '.join(string_rep)

    '''
    Construction works by reading a line from the csv and creating or extending nodes in the trie according to its
    letters.
    Simultaneously, using the best_children min heap the best results are maintained.
    '''

    @staticmethod
    def construct(input_file, skip_java_identifier_check=False):
        names_file = open(input_file, 'r')
        name_reader = csv.reader(names_file)
        name_trie = NameTrieNode()
        for row in name_reader:
            name = row[0]
            if not skip_java_identifier_check and not is_valid_java_identifier(name):
                continue
            score = int(row[1])
            trie = name_trie
            for char in name:
                trie = trie.get_next_child(char, name, score)
                if char == '_':
                    name_trie.underscore_children.add(trie)
            trie.add_leaf(name, score)
        return name_trie

    def get_next_child(self, char, name, score):
        if char not in self.children:
            new_trie_node = NameTrieNode(char)
            self.children[char] = new_trie_node
            self.num_of_children += 1
        else:
            new_trie_node = self.children[char]
        self._add_best_child(name, score)
        return new_trie_node

    def _add_best_child(self, name, score):
        if len(self.best_children) < self.MAX_RESULT_SIZE:
            heappush(self.best_children, (score, name))
        else:
            heappushpop(self.best_children, (score, name))

    def add_leaf(self, name, score):
        if self.END_CHAR not in self.children:
            self.children[self.END_CHAR] = NameTrieLeaf(name, score)
            self._add_best_child(name, score)

    '''
    Serialized using a pre order traversal of the trie
    Done iteratively to avoid to avoid too deep a recursive stack
    Can be improved a lot
    '''

    def serialize(self):
        serial = []
        stack = [self]
        while len(stack) != 0:
            trie_node = stack.pop()
            serial.append(str(trie_node))
            if trie_node.children:
                for char, node in trie_node.children.iteritems():
                    stack.append(node)
        serial_file_name = 'serialized'
        serial_file = open(serial_file_name, 'w')
        serial_file.write('\n'.join(serial))
        serial_file.close()
        return serial_file_name

    '''
    Deserialized reading line by line using a stack
    Done iteratively to avoid to avoid too deep a recursive stack
    '''

    @staticmethod
    def deserialize(serialized_file_name):
        serialized_file = open(serialized_file_name, 'r')
        stack = []
        root_node = NameTrieNode.construct_single_node(serialized_file.readline())
        stack.append(root_node)
        for line in serialized_file:
            trie_node = NameTrieNode.construct_single_node(line)
            stack.append(trie_node)
            if line[0] == '_':
                root_node.underscore_children.add(trie_node)
        serialized_file.close()
        orphan_nodes = []
        while len(stack) != 0:
            trie_node = stack.pop()
            if trie_node.children is None:
                orphan_nodes.append(trie_node)
            else:
                if len(trie_node.children) == trie_node.num_of_children:
                    orphan_nodes.append(trie_node)
                else:
                    while len(trie_node.children) != trie_node.num_of_children:
                        node = orphan_nodes.pop()
                        if node.children is None:
                            trie_node.children[NameTrieNode.END_CHAR] = node
                        else:
                            trie_node.children[node.char] = node
                    orphan_nodes.append(trie_node)
        return root_node


    @staticmethod
    def construct_single_node(serialized_node):
        node_parts = serialized_node.split(' ')
        char = node_parts[0]
        if char == NameTrieNode.END_CHAR:
            score = int(node_parts[1])
            if node_parts[2][-1] == '\n':
                name = node_parts[2][:-1]
            else:
                name = node_parts[2]
            return NameTrieLeaf(name, score)
        else:
            num_of_children = int(node_parts[2])
            best_children_string = node_parts[1].split('|')
            best_children = []
            for child in best_children_string:
                child_tuple = child.split(',')
                best_children.append((int(child_tuple[0]), child_tuple[1]))
            trie_node = NameTrieNode(char)
            trie_node.num_of_children = num_of_children
            trie_node.best_children = best_children
            return trie_node


    def get_best_children(self, prefix):
        trie = self
        for letter in prefix:
            if letter in trie.children:
                trie = trie.children[letter]
            else:
                return []
        return list(trie.best_children)


class NameTrieLeaf:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.children = None

    def __str__(self):
        return '# ' + str(self.score) + ' ' + self.name

