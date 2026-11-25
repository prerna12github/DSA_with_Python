class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = n - 1
        result = 0
        nums.sort()
        while i < j:
            summ = nums[i] + nums[j]
            result = max(result,summ)
            i = i + 1
            j = j - 1
        return result    

        