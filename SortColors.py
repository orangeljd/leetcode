class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        for i in range(right + 1):
            while nums[i] == 2 and i < right:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            while nums[i] == 0 and i > left:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1

t = Solution()
t.sortColors([1, 2, 0])