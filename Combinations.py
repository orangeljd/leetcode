class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.combination(n, 1, k, [], res)
        return res

    def combination(self,n ,cur, k, tmp, res):
        if k == 0:
            res.append(tmp[:])
            return
        for i in range(cur, n - k + 2):
            self.combination(n, i + 1, k - 1, tmp + [i], res)

t = Solution()
print(t.combine(3, 2))