class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left  = 0
        zeroes  = 0
        max_len = 0
        for right in range(n):
            if nums[right] == 0 :
                zeroes = zeroes + 1
            if zeroes > k :
                if nums[left] == 0:
                  zeroes = zeroes - 1
                left = left + 1  
        max_len = max(max_len , right-left + 1)
        return max_len           
        