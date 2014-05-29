__author__ = 'aanurag'

import sys
from binary_tree import BinaryTree


class IntervalTree(BinaryTree):
    def __init__(self):
        BinaryTree.__init__(self)
        self.max = None

    def insert(self, key, parent=None):
        try:
            if (self.key == None):
                self.key = key
                self.parent = parent
                self.max = key[1]
                return self
            elif (self.key == key):
                return
            elif (key[0] > self.key[0]):
                self.max = max(self.max, key[1])
                if (self.right == None):
                    self.right = IntervalTree()
                return self.right.insert(key, self)
            else:
                self.max = max(self, key[1])
                if (self.left == None):
                    self.left = IntervalTree()
                return self.left.insert(key, self)
        except TypeError as e:
                print "Expected tuple, didn't find it."


    def delete(self, key):
        if (self.key == key):
            #leaf
            if self.left == None and self.right == None:
                self.key = None
            #only right subtree
            elif self.left == None:
                node = self.right
                self.key = node.key
                self.left = node.left
                self.right = node.right
                if self.left:
                    self.left.parent = self
                if self.right:
                    self.right.parent = self
            #only left subtree
            elif self.right == None:
                node = self.left
                self.key = node.key
                self.left = node.left
                self.right = node.right
                if self.left:
                    self.left.parent = self
                if self.right:
                    self.right.parent = self
            #both subtrees
            else:
                #smallest node in right subtree
                smallest_node = self.right
                while (smallest_node.left != None):
                    smallest_node = smallest_node.left
                self.key, smallest_node.key = smallest_node.key, self.key
                smallest_node.delete(key)
            self.updateMax()
        elif (key[0] > self.key[0] and self.right != None):
            self.right.delete(key)
        elif self.left != None:
            self.left.delete(key)

    def updateMax(self):
        node = self
        while node.parent != None:
            if node.left and node.right:
                node.max = max(node.max, node.left.max, node.right.max)
            elif node.left:
                node.max = max(node.max, node.left.max)
            elif node.right:
                node.max = max(node.max, node.right.max)
            node = node.parent

    def findOverlapping(self, key):
        node = self
        while node and (node.key[0] >= key[1] or node.key[1] < key[0]):
            if node.left and key[0] < node.left.max:
                node = node.left
            elif node.right:
                node = node.right
            else:
                node = None
        if node:
            return node.key
        else:
            return None

    def inorder(self, inorder_opt=None):
        if inorder_opt is None:
            inorder_opt = []
        if (self.left != None):
            self.left.inorder(inorder_opt)
        if (self.key != None):
            inorder_opt.append(str(self.key) + '{' + str(self.max) + '}')
        if (self.right != None):
            self.right.inorder(inorder_opt)
        return inorder_opt


def main():
    arr = [45, 18, 81, 65, 3, 79, 23, 5, 4, 78]
    print(arr)
    BST = IntervalTree()
    # for i in range(len(arr)):
    #     BST.insert(())
    BST.insert((17,19))
    BST.insert((5,11))
    BST.insert((4,8))
    BST.insert((15,18))
    BST.insert((7,10))
    BST.insert(21,23)
    print(BST.inorder())
    # BST.delete((5,8))
    print(BST.findOverlapping((14,16)))
    print(BST.findOverlapping((12,14)))


if __name__ == "__main__":
    sys.exit(main())
