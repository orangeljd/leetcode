class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        for i in range(len(matrix)):
            if target <= matrix[i][-1]: break
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            cur = (left + right) // 2
            if target < matrix[i][cur]: right = cur - 1
            elif target > matrix[i][cur]: left = cur + 1
            else: break
        return matrix[i][cur] == target

t = Solution()
print(t.searchMatrix([[1]], 2))