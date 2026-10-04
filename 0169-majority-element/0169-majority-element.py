class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            if count == 0:
                count = 1
                cand = nums[i]
            elif cand == nums[i]:
                count = count + 1
            else:
                count = count - 1
        return cand                 
        