__author__ = 'aanurag'

import sys
from binary_tree import BinaryTree

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
        if not self.areAllNodesColored():
            print "Not all nodes colored!"
            return
        if not self.areRootAndLeavesBlack():
            print "Root or leaf is not black!!"
            return
        if not self.isParentOfEveryRedNodeBlack():
            print "Red node with red child!!!"
            return
        #missing checking the constant black length property
        print "All good"
        return


    def RBinorder(self, inorder_opt=None):
        if inorder_opt is None:
            inorder_opt = []
        if (self.left != None):
            self.left.RBinorder(inorder_opt)
        if (self.key != None):
            inorder_opt.append(str(self.key) + str(self.color))
        if (self.right != None):
            self.right.RBinorder(inorder_opt)
        return inorder_opt


def main():
    arr = [45, 18, 81, 65, 3, 79, 23, 5, 4, 78]
    print(arr)
    BST = RBTree()
    for i in range(len(arr)):
        BST.RBinsert(arr[i])
    print(BST.RBinorder())
    BST.checkRBProps()
    #missing RBdelete function hence using base class's delete, may not preserve RB props in all cases
    BST.delete(45)
    print(BST.RBinorder())
    BST.checkRBProps()

if __name__ == "__main__":
    sys.exit(main())