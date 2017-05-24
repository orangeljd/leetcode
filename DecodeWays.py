class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for i in range(len(s))]
        if dp == []: return 0
        for i, c in enumerate(s):
            if i == 0:
                dp[i] = int(c != '0')
            elif i == 1:
                dp[i] = (c != '0' and dp[i - 1] or 0) + (s[i - 1] != '0' and 0 < int(s[i - 1: i + 1]) <= 26 and 1 or 0)
            else:
                dp[i] = (c != '0' and dp[i - 1] or 0) + (s[i - 1] != '0' and 0 < int(s[i - 1: i + 1]) <= 26 and dp[i - 2] or 0)
        return dp[-1]

t = Solution()
print(t.numDecodings('101'))