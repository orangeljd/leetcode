class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = x // 2
        left, right = 0, x
        while True:
            tmp = res ** 2
            if tmp == x: return res
            elif tmp > x: right = res - 1
            elif (res + 1) ** 2 > x: return res
            else: left = res + 1
            res = (left + right) // 2