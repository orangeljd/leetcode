class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, numsLen = [[]], len(nums)
        nums.sort()
        def subset(cur, tmp):
            if cur == numsLen: return
            for i in range(cur, numsLen):
                if i > cur and nums[i] == nums[i - 1]: continue
                subset(i + 1, tmp + [nums[i]])
                res.append(tmp + [nums[i]])
        subset(0, [])
        return res

t = Solution()
print(t.subsetsWithDup([1,2,2]))