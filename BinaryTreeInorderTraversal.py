# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root: return (root.left and self.inorderTraversal(root.left) or []) + [root.val] + (root.right and self.inorderTraversal(root.right) or [])
        else: return []