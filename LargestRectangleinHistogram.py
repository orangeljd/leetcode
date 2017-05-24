class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        res = 0
        heights.append(0)
        for i in range(len(heights)):
            while len(stack) != 0 and heights[stack[-1]] > heights[i]:
                h = heights[stack[-1]]
                del(stack[-1])
                l = len(stack) == 0 and i or i - stack[-1] - 1
                res = max(res, h * l)
            stack.append(i)
        return res

t = Solution()
print(t.largestRectangleArea([2,1,5,6,2,3]))