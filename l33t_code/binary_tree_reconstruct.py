# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def linear_search(arr, search):
    for index,el in enumerate(arr):
        if el == search:
            return index
    return None


class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        len_inorder = len(inorder)
        len_postorder = len(postorder)
        if len(inorder) == 0 or len(postorder) == 0:
            return None

        root_val = postorder[len_postorder - 1]
        root = TreeNode(root_val)
        root_index = linear_search(inorder, root_val)
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:]

        right_size = len_inorder - 1 - root_index
        left_postorder = postorder[:len_postorder - 1 - right_size]
        right_postorder = postorder[len_postorder - 1 - right_size:-1]

        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root
        