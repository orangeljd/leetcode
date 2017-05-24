# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return n != 0 and self.__generate(1, n) or []

    def __generate(self, left, right):
        """
        :param left:
        :param right:
        :return:
        """
        if left > right: return [None]
        elif left == right: return [TreeNode(left)]
        res = []
        for i in range(left, right + 1):
            leftChildren = self.__generate(left, i - 1)
            rightChildren = self.__generate(i + 1, right)
            for leftChild in leftChildren:
                for rightChild in rightChildren:
                    cur = TreeNode(i)
                    cur.left = leftChild
                    cur.right = rightChild
                    res.append(cur)
        return res