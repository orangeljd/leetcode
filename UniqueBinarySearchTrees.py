class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n + 1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, (i + 1) // 2 + 1):
                dp[i] += (2 - int(j == (i + 1) // 2 and i % 2 == 1)) * dp[j - 1] * dp[i - j]
        return dp[-1]


t = Solution()
for i in range(1, 5):
    print(t.numTrees(i))