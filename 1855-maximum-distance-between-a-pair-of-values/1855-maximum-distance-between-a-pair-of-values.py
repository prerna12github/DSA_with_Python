class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:

        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        result = 0
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                i = i + 1
            else:
                result = max(result,j-i)
                j = j + 1
        return result            
