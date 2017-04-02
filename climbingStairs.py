class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        elif n == 1: return 1
        elif n == 2: return 2
        dp = [None for i in range(n)]
        dp[0], dp[1] = 1, 2
        for i in range(2, n): dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n - 1]