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

class RBTree(BinaryTree):
    def __init__(self):
        BinaryTree.__init__(self)
        self.color = None

    def insert(self, key, parent=None):
        if (self.key == None):
            self.key = key
            self.parent = parent
            return self
        elif (self.key == key):
            return
        elif (key > self.key):
            if (self.right == None):
                self.right = RBTree()
            return self.right.insert(key, self)
        else:
            if (self.left == None):
                self.left = RBTree()
            return self.left.insert(key, self)

    def RBinsert(self, key):
        x_node = self.insert(key)
        x_node.color = 'R'
        while x_node and x_node.parent != None and x_node.color == 'R':
            x_parent = x_node.parent
            x_grandparent = x_parent.parent
            if not x_grandparent: break
            #A: if parent is left of grand parent
            if x_parent == x_grandparent.left:
                y_node = x_node.parent.parent.right  #uncle of x_node
                #Case1: Recolor
                if x_parent.color == 'R':
                    if y_node and y_node.color == 'R':
                        x_parent.color = y_node.color = 'B'
                        x_grandparent.color = 'R'
                    #Case 2/3
                    else:
                        #Case2: Left rotate x_parent
                        if x_node == x_node.parent.right:
                            x_node.left_rotate()
                        #Case3: Right rotate x_parent
                        x_node.right_rotate()
                        x_node.color = 'B'
                        x_node.right.color = 'R'
                x_node = x_node.parent.parent
            #B: if parent is right of grand parent
            else:
                y_node = x_node.parent.parent.left  #uncle of x_node
                #Case1: Recolor
                if x_parent.color == 'R':
                    if y_node and y_node.color == 'R':
                        x_parent.color = y_node.color = 'B'
                        x_grandparent.color = 'R'
                        #move to gparent
                    #Case 2/3
                    else:
                        #Case2: Left rotate x_parent
                        if x_node == x_node.parent.left:
                            x_node.right_rotate()
                        #Case3: Right rotate x_parent
                        x_node.left_rotate()
                        x_node.color = 'B'
                        x_node.left.color = 'R'
                x_node = x_node.parent.parent
        self.color = 'B'

    def left_rotate(self):
        parent = self.parent
        self.parent = parent.parent
        if parent == parent.parent.left:
            parent.parent.left = self
        else:
            parent.parent.right = self
        parent.right = self.left
        self.left = parent
        parent.parent = self
        #return self

    def right_rotate(self):
        parent = self.parent
        self.parent = parent.parent
        if parent == parent.parent.left:
            parent.parent.left = self
        else:
            parent.parent.right = self
        parent.left = self.right
        self.right = parent
        parent.parent = self
        #return self

    def areAllNodesColored(self):
        if self.key == None:
            return True
        elif self.color != None:
            left_check = right_check = True
            if self.left:
                left_check = self.left.areAllNodesColored()
            if self.right:
                right_check = self.right.areAllNodesColored()
            return left_check and right_check
        else:
            return False

    def areRootAndLeavesBlack(self):
        if self.parent == None and self.color != 'B':
            return False
        else:
            left_check = right_check = True
            if self.left:
                left_check = self.left.areRootAndLeavesBlack()
            if self.right:
                right_check = self.right.areRootAndLeavesBlack()
            return left_check and right_check

    def isParentOfEveryRedNodeBlack(self):
        if self.color == 'R' and self.parent and self.parent.color != 'B':
            return False
        else:
            left_check = right_check = True
            if self.left:
                left_check = self.left.isParentOfEveryRedNodeBlack()
            if self.right:
                right_check = self.right.isParentOfEveryRedNodeBlack()
            return left_check and right_check

    def checkRBProps(self):
        if not self.areAllNodesColored(): print "Not all nodes colored!"
        if not self.areRootAndLeavesBlack(): print "Root or leaf is not black!!"
        if not self.isParentOfEveryRedNodeBlack(): print "Red node with red child!!!"

    def RBinorder(self, inorder_opt=None):
        if inorder_opt is None:
            inorder_opt = []
        if (self.left != None):
            self.left.RBinorder(inorder_opt)
        if (self.key != None):
            inorder_opt.append(str(self.key) + self.color)
        if (self.right != None):
            self.right.RBinorder(inorder_opt)
        return inorder_opt


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
