class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        count = collections.Counter()
        countsum, numsLen = 0, len(nums)
        for i in range(numsLen - 1, -1, -1):
            if count[nums[i]] <2:
                count[nums[i]] += 1
                countsum += 1
            else:
                del(nums[i])
        return countsum

t = Solution()
print(t.removeDuplicates([1, 1 ,1]))