class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        while k >= 0:
            while j >= 0 and (i >= 0 and nums2[j] > nums1[i] or i == -1):
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
            while i >= 0 and (j >= 0 and nums1[i] >= nums2[j] or j == -1):
                nums1[k] = nums1[i]
                i -= 1
                k -= 1

t = Solution()
nums1 = [0]
t.merge(nums1, 0, [1], 1)
print(nums1)