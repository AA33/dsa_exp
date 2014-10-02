__author__ = 'aanurag'

import sys


class BinaryTree:
    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, key, parent=None):
        if self.key is None:
            self.key = key
            self.parent = parent
            return self
        elif self.key == key:
            return
        elif key > self.key:
            if self.right is None:
                self.right = BinaryTree()
            return self.right.insert(key, self)
        else:
            if self.left is None:
                self.left = BinaryTree()
            return self.left.insert(key, self)

    def isEmptyLeaf(self):
        if self.key is None and self.left is None and self.right is None:
            return True
        else:
            return False

    def delete(self, key):
        if self.key == key:
            # leaf
            if self.left is None and self.right is None:
                self.key = None
            # only right subtree
            elif self.left is None:
                node = self.right
                self.key = node.key
                self.left = node.left
                self.right = node.right
                if self.left:
                    self.left.parent = self
                if self.right:
                    self.right.parent = self
            # only left subtree
            elif self.right is None:
                node = self.left
                self.key = node.key
                self.left = node.left
                self.right = node.right
                if self.left:
                    self.left.parent = self
                if self.right:
                    self.right.parent = self
            # both subtrees
            else:
                # smallest node in right subtree
                smallest_node = self.right
                while smallest_node.left is not None:
                    smallest_node = smallest_node.left
                self.key, smallest_node.key = smallest_node.key, self.key
                smallest_node.delete(key)
        elif key > self.key and self.right is not None:
            self.right.delete(key)
        elif self.left is not None:
            self.left.delete(key)


    def search(self, key):
        if self.key == key:
            return True
        elif key > self.key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        else:
            return False

    def inorder(self, inorder_opt=None):
        if inorder_opt is None:
            inorder_opt = []
        if self.left is not None:
            self.left.inorder(inorder_opt)
        if self.key is not None:
            inorder_opt.append(self.key)
        if self.right is not None:
            self.right.inorder(inorder_opt)
        return inorder_opt


    def size(self, size=0):
        if self:
            if self.left:
                size += self.left.size()
            if self.right:
                size += self.right.size()
            return size + 1
        else:
            return 0

    def kth_smallest(self, k):
        left_size = 0
        if self.left:
            left_size = self.left.size()
        cur_rank = left_size + 1
        if cur_rank == k:
            return self.key
        elif self.left and cur_rank > k:
            return self.left.kth_smallest(k)
        elif self.right:
            return self.right.kth_smallest(k - cur_rank)
        else:
            return None

    def least_common_ancestor(self, p, q):
        if self is None:
            return None
        if self == p or self == q:
            return self
        else:
            if self.left:
                left_lca = self.left.least_common_ancestor(p, q)
            else:
                left_lca = None
            if self.right:
                right_lca = self.right.least_common_ancestor(p, q)
            else:
                right_lca = None
            if left_lca and right_lca:
                return self
            elif left_lca:
                return left_lca
            else:
                return right_lca

    def get_level_map(self):
        dict = {}
        self._get_lmap(dict, 0)
        return dict

    def _get_lmap(self, level_dict, level):
        if level in level_dict:
            level_dict[level].append(self.key)
        else:
            level_dict[level] = [self.key]
        if self.left:
            self.left._get_lmap(level_dict, level + 1)
        if self.right:
            self.right._get_lmap(level_dict, level + 1)

    def get_max_path_sum(self):
        max_root, max_other = self._get_max_path_sum()
        return max_root

    def _get_max_path_sum(self):
        left_sum = right_sum = left_root = right_root = 0
        if self.left:
            left_root, left_sum = self.left._get_max_path_sum()
        if self.right:
            right_root, right_sum = self.right._get_max_path_sum()
        self_root = self.key + left_sum + right_sum

        if self_root > left_root and self_root > right_root:
            part1 = self_root
        elif left_root > self_root and left_root > right_root:
            part1 = left_root
        else:
            part1 = right_root

        if left_sum > right_sum:
            part2 = left_sum + self.key
        else:
            part2 = right_sum + self.key

        return part1, part2


def main():
    arr = [45, 18, 81, 65, 3, 79, 23, 5, 4, 78]
    print(arr)
    BST = BinaryTree()
    for i in range(len(arr)):
        BST.insert(arr[i])
    print(BST.inorder())
    print(BST.least_common_ancestor(BST.left.left.right, BST.left.right).key)
    print(BST.least_common_ancestor(BST.right.left.right, BST.right.left.right.left).key)
    print BST.get_level_map()
    # print(BST.kth_smallest(10))
    # BST = RBTree()
    # for i in range(len(arr)):
    # BST.RBinsert(arr[i])
    # BST.checkRBProps()
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
    # BST.delete(45)
    # BST.delete(23)
    # BST.delete(81)
    # print(BST.inorder())
    # BST.delete(54)
    # print(BST.inorder())
    BT = BinaryTree()
    BT.key = 8
    BT.left = BinaryTree()
    BT.left.key = 7
    BT.right = BinaryTree()
    BT.right.key = 23
    left = BT.left
    left.left = BinaryTree()
    left.left.key = 15
    left.right = BinaryTree()
    left.right.key = 9
    right = BT.right
    right.left = BinaryTree()
    right.left.key = 2
    right.right = BinaryTree()
    right.right.key = 1

    print(BT.get_max_path_sum())


if __name__ == "__main__":
    sys.exit(main())
