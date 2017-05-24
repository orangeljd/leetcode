class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        if row == 0: return 0
        column = len(matrix[0])
        if column == 0: return 0
        dp = [0 for i in range(column + 1)]
        res = 0
        for i in range(row):
            stack = []
            for j in range(column + 1):
                if j < column: dp[j] = matrix[i][j] != '0' and int(matrix[i][j]) + dp[j] or 0
                while len(stack) != 0 and dp[stack[-1]] > dp[j]:
                    h = dp[stack[-1]]
                    del(stack[-1])
                    l = len(stack) == 0 and j or j - stack[-1] - 1
                    res = max(res, h * l)
                stack.append(j)
        return res

t = Solution()
print(t.maximalRectangle(["10100","10111","11111","10010"]))