class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0: return [0]
        return list(map(int, self.genGrayCode(n), [2 for i in range(2 ** n)]))

    def genGrayCode(self, n):
        if n == 1: return ['0', '1']
        res = []
        tmp = self.genGrayCode(n - 1)
        for i in tmp:
            res += ['0' + i]
        for i in reversed(tmp):
            res += ['1' + i]
        return res

t = Solution()
print(t.grayCode(2))