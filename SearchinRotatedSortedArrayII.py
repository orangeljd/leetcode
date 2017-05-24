class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]: return True
            if nums[mid] > nums[left]:
                if target >= nums[left] and target < nums[mid]: right = mid - 1
                else: left = mid + 1
            elif nums[mid] < nums[left]:
                if target <= nums[right] and target > nums[mid]: left = mid + 1
                else: right = mid - 1
            else:
                right -= 1
        return target == nums[mid] and True or False

t = Solution()
print(t.search([1,3, 1, 1,1], 3))