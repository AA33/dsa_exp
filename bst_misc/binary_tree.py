__author__ = 'aanurag'

import sys


class BinaryTree:
    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, key, parent=None):
        if (self.key == None):
            self.key = key
            self.parent = parent
            return self
        elif (self.key == key):
            return
        elif (key > self.key):
            if (self.right == None):
                self.right = BinaryTree()
            return self.right.insert(key, self)
        else:
            if (self.left == None):
                self.left = BinaryTree()
            return self.left.insert(key, self)

    def isEmptyLeaf(self):
        if (self.key == None and self.left == None and self.right == None):
            return True
        else:
            return False

    def delete(self, key):
        if (self.key == key):
            #leaf
            if self.left == None and self.right == None:
                self.key =None
            #only right subtree
            elif self.left == None:
                node =  self.right
                self.key = node.key
                self.left = node.left
                self.right = node.right
                if self.left:
                    self.left.parent = self
                if self.right:
                    self.right.parent = self
            #only left subtree
            elif self.right == None:
                node =  self.left
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
        elif (key > self.key and self.right != None):
            self.right.delete(key)
        elif self.left != None:
            self.left.delete(key)


    def search(self, key):
        if (self.key == key):
            return True
        elif (key > self.key and self.right != None):
            return self.right.search(key)
        elif self.left != None:
            return self.left.search(key)
        else:
            return False

    def inorder(self, inorder_opt=None):
        if inorder_opt is None:
            inorder_opt = []
        if (self.left != None):
            self.left.inorder(inorder_opt)
        if (self.key != None):
            inorder_opt.append(self.key)
        if (self.right != None):
            self.right.inorder(inorder_opt)
        return inorder_opt


    def size(self,size=0):
        if self:
            if self.left:
                size +=self.left.size()
            if self.right:
                size +=self.right.size()
            return size+1
        else:
            return 0

    def kth_smallest(self, k):
        left_size = 0
        if self.left:
            left_size = self.left.size()
        cur_rank = left_size +1
        if cur_rank == k:
            return self.key
        elif self.left and cur_rank > k:
            return self.left.kth_smallest(k)
        elif self.right:
            return self.right.kth_smallest(k - cur_rank)
        else:
            return None

def main():
    arr = [45, 18, 81, 65, 3, 79, 23, 5, 4, 78]
    print(arr)
    BST = BinaryTree()
    for i in range(len(arr)):
        BST.insert(arr[i])
    print(BST.inorder())
    # print(BST.kth_smallest(10))
    # BST = RBTree()
    # for i in range(len(arr)):
    #     BST.RBinsert(arr[i])
    #     BST.checkRBProps()
    # print(BST.RBinorder())
    # print(BST.kth_smallest(10))
    # print(BST.search(91))
    # print(BST.search(18))
    # BST.insert(4)
    # BST.insert(2)
    # BST.insert(1)
    # BST.insert(3)
    # BST.insert(6)
    # BST.insert(5)
    # BST.insert(7)
    # print(BST.inorder())
    # BST = BST.delete(1)
    BST.delete(45)
    BST.delete(23)
    BST.delete(81)
    print(BST.inorder())
    BST.delete(54)
    print(BST.inorder())


if __name__ == "__main__":
    sys.exit(main())
